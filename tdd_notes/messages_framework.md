# Testing with the messages framework

- we have to pass follow=True to the test client to tell it to get the page after the 302-redirect 

```python
def test_adds_success_message(self):
        response = self.client.post('/accounts/send_login_email', data={
            'email': 'edith@example.com'
        }, follow=True)

        message = list(response.context['messages'])[0]  # we must 'listify' the context of the response
        self.assertEqual(
            message.message,
            "Check your email, we've sent you a link you can use to log in."
        )
        self.assertEqual(message.tags, "success")
```

- it is not recommended to test messages framework with mocking because the messages framework gives you more than one
 way to achieve the same result
 
```python
from django.contrib import messages
# either this way
messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )

# or this way
messages.add_message(
        request,
        messages.SUCCESS,
        "Check your email, we've sent you a link you can use to log in."
    )
```

- if we wanted to use mocking anyway, this is a test for the first implementation ONLY
```python
from unittest.mock import patch, call

    @patch('accounts.views.messages')
    def test_adds_success_message_with_mocks(self, mock_messages):
        response = self.client.post('/accounts/send_login_email', data={
            'email': 'edith@example.com'
        })

        expected = "Check your email, we've sent you a link you can use to log in."
        self.assertEqual(
            mock_messages.success.call_args,
            call(response.wsgi_request, expected),
        )
```

- this is a typical HTML boilerplate for bootstrap
```html
{% if messages %}
    <div class="row">
      <div class="col-md-8">
        {% for message in messages %}
          {% if message.level_tag == 'success' %}
            <div class="alert alert-success">{{ message }}</div>
          {% else %}
            <div class="alert alert-warning">{{ message }}</div>
          {% endif %}
        {% endfor %}
      </div>
    </div>
  {% endif %}
```