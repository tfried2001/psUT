import random

class SingleSignOnRegistry:

    def register_new_session(self, credentials):
        """Returns an instance of SSOToken if the credentials are valid"""
        pass

    def is_valid(self, token):
        """Returns True if the token refers to a current session"""
        pass

    def unregister(self, token):
        """Removes the given token from current sessions"""
        pass

class SSOToken:
    def __init__(self, *args, **kwargs):
        self.id = random.randrange(100000)

    def __eq__(self, value):
        return self.id == value.id

    def __repr__(self):
        return str(self.id)

