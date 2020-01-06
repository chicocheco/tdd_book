# Alternative use of mocks - reducing duplication
- mocks can save you from duplication in your tests
- the nonmocky way of testing a login view would be to see whether it does actually log the user in, 
by checking whether the user gets assigned an authenticated session cookie in the right circumstances
- `call()` is a helper object we can use to check whether a mocked function was called with some particular arguments.
It is basically a shortcut to `.call_args` property of a mock
- it's not recommended to use a magical `.assert_called_with(foo, bar)` because it's easy to do it wrong

```python
from unittest.mock import patch, call

    @patch('accounts.views.auth')  
    def test_calls_authenticate_with_uid_from_get_request(self, mock_auth):  
        self.client.get('/accounts/login?token=abcd123')
        self.assertEqual(
            mock_auth.authenticate.call_args,  # how was authenticate() called
            call(uid='abcd123')  # called with key argument uid with value 'abcd123'?   
            # call(uid='abcd123') is equal to ((,), {'uid': 'abcd123'})
        )
```

## copy of returned mock of a mock
- `.return_value`: The value returned when the mock is called. By default this is a new Mock (created on first access)
- when you call a mock, you get another mock. But you can also get a copy of that returned mock from the original mock 
that you called
# TODO: I dont fucking get it
```
>>> m = Mock()
>>> thing = m()
>>> thing
<Mock name='mock()' id='140652722034952'>
>>> m.return_value
<Mock name='mock()' id='140652722034952'>
>>> thing == m.return_value
True
m
<Mock id='139885547169608'>
m.return_value = 'fish'
m
<Mock id='139885547169608'>
m
<Mock id='139885547169608'>
m()
'fish'
```
- here we use to test whether the `auth.login()` was called with an instance of our User model object
```python
from unittest.mock import patch, call

    @patch('accounts.views.auth')  
    def test_calls_auth_login_with_user_if_there_is_one(self, mock_auth):
        response = self.client.get('/accounts/login?token=abcd123')
        self.assertEqual(
            mock_auth.login.call_args,  # how was login() called
            call(response.wsgi_request, mock_auth.authenticate.return_value)  # called with request passed to the view 
            # and with what our custom authentication backend returns - instance of User?  
        )
```

## Patching at class level, explicitly setting up return value of a mock to None
- "three strikes" rule - move the patch to the class level
- we can also set up the return value of a mock to `None` by hand, to test if our code works with that too
```python
@patch('accounts.views.auth')  
class LoginViewTest(TestCase):

    def test_redirects_to_home_page(self, mock_auth):  
        [...]

    def test_calls_authenticate_with_uid_from_get_request(self, mock_auth):  
        [...]

    def test_calls_auth_login_with_user_if_there_is_one(self, mock_auth):  
        [...]


    def test_does_not_login_if_user_is_not_authenticated(self, mock_auth):
        mock_auth.authenticate.return_value = None  
        self.client.get('/accounts/login?token=abcd123')
        self.assertEqual(mock_auth.login.called, False)  # testing the if clause in login()
```