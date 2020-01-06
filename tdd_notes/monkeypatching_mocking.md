# Monkeypatching or manual mocking
- a mock is used to simulate the third-party API
- for example how to test sending email emails without sending emails - replace the send_mail function with a 
fake version, at runtime
- one way is manual mocking (monkeypatching) which can cause problems when not returning the original function back 
after it was "mocked out" 
```python
def test_sends_mail_to_address_from_post(self):
        self.send_mail_called = False
        
        # without using the mock library, monkeypatching:
        def fake_send_mail(subject, body, from_email, to_list):  
            self.send_mail_called = True
            self.subject = subject
            self.body = body
            self.from_email = from_email
            self.to_list = to_list
        
        accounts.views.send_mail = fake_send_mail  # replace it for a fake version here
        # after this line, send_mail is "mocked out" and we assert self.subject etc.
```
- but there is a neater way - the Python Mock library
# The mock library
- we can call the parameter of a mock anyhow but by convenience it is `mock_` + mocked function
- the `.call_args` property on a mock represents the positional and keyword arguments that the mock was called with. 
It’s a special "call" object type, which is essentially a tuple of (positional_args_tuple, keyword_args_dict). 
It is convenient to unpack its first member to extract a value of each argument to do assertions 
- `.call()`is a helper object for making simpler assertions, for comparing with `.call_args`
- `.return_value`: The value returned when the mock is called. By default this is a new Mock (created on first access)
which is not always desirable 

```python
from django.test import TestCase
from unittest.mock import patch

    @patch('accounts.views.send_mail')  # this injects a faked version into the test but returns the original afterwards
    def test_sends_mail_to_address_from_post(self, mock_send_mail):  # we can call it mock_*
        self.client.post('/accounts/send_login_email', data={
            'email': 'edith@example.com'
        })

        self.assertEqual(mock_send_mail.called, True)  # to be sure we called it
        # here we *unpack* the positional arguments
        # notice that call_args is a tuple consisting of 1 tuple and 1 dict ((positional_args), {keyword_args})  
        (subject, body, from_email, to_list), kwargs = mock_send_mail.call_args 
        self.assertEqual(subject, 'Your login link for Superlists')
        self.assertEqual(from_email, 'noreply@superlists')
        self.assertEqual(to_list, ['edith@example.com'])
```