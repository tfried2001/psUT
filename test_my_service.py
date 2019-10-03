from my_service import MyService, Request
from single_sign_on import SSOToken, SingleSignOnRegistry

from unittest.mock import Mock
import pytest


@pytest.fixture
def sso_registry():
    """Provides a mock SingleSignOnRegistry object"""
    sso_registry = Mock(SingleSignOnRegistry)
    return sso_registry

@pytest.fixture
def token():
    """Provides an initialized SSOToken"""
    token = SSOToken()
    return token


def test_hello_name(sso_registry, token):
    service = MyService(sso_registry)
    response = service.handle(Request("Emily"), token)
    assert response.text == "Hello Emily!"

def test_single_sign_on_with_valid_token(sso_registry, token):
    service = MyService(sso_registry)
    service.handle(Request("Emily"), token)
    sso_registry.is_valid.assert_called_with(token)

def test_single_sign_on_with_invalid_token(sso_registry, token):
    sso_registry.is_valid.return_value = False
    service = MyService(sso_registry)
    response = service.handle(Request("Emily"), token)
    sso_registry.is_valid.assert_called_with(token)
    assert response.text == "Please sign in"

def confirm_token(correct_token):
    def is_valid(actual_token):
        if actual_token != correct_token:
            raise ValueError("Wrong token received")
    return is_valid

def test_single_sign_on_receives_correct_token(sso_registry, token):
    sso_registry.is_valid = Mock(side_effect=confirm_token(token))
    service = MyService(sso_registry)
    service.handle(Request("Emily"), token)
    sso_registry.is_valid.assert_called()

