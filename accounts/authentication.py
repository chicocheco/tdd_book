from accounts.models import User, Token


class PasswordlessAuthenticationBackend:

    # django requires to create an instance of this class although there is no __init__
    # we must therefore execute it with PasswordlessAuthenticationBackend() - parentheses
    def authenticate(self, request=None, uid=None):
        try:
            token = Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            return User.objects.create(email=token.email)
        except Token.DoesNotExist:
            return None

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
