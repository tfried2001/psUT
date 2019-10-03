from my_service import MyService, Request
from single_sign_on import SSOToken

def test_hello_name():
    service = MyService(None)
    response = service.handle(Request("Emily"), SSOToken())
    assert response.text == "Hello Emily!"

