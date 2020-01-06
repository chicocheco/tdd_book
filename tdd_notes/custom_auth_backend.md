# Custom authentication backend 

- we take a UID and check if it exists in the database (Token model)
- we return None if it does not
- if it does exist, we extract an email address, and either find an existing user with that address, 
or create a new one

We work with two models here: User and Token
- Token stores email and uid (new uid is generated with every sent email - a lot of rows)
- User stores email (and it's primary key at the same time - only few rows)
```python
class PasswordlessAuthenticationBackend:

    def authenticate(self, request=None, uid=None):
        try:
            token = Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)  # when the email is both in Token and User model
        except User.DoesNotExist:
            return User.objects.create(email=token.email)  # if that email is not in User model yet, add it
        except Token.DoesNotExist:
            return None

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

```

- in authenticate() we have 2 try/excepts blocks and one if clause, we need 3 tests
- in the second part of the protocol get_user() we need 2 tests

- we also must enable the custom auth backend in `settings.py`
```python
AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = [
    'accounts.authentication.PasswordlessAuthenticationBackend',
]
```