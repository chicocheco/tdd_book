# building URI in Django

- creating a new URL with a `token` GET parameter `?<name_of_parameter>=`  
```python
# where
url = request.build_absolute_uri(  
        reverse('login') + '?token=' + str(token.uid)
    )
```

- when opening this kind of URL, the `token` parameter can be read in a GET request
```python
user = auth.authenticate(uid=request.GET.get('token'))
```