# Deployment notes

## Preparation
- get a domain name
- get an Ubuntu server with root SSH access and note its IP address
- point both the domain and staging subdomain to the IP of the server
- open a port 80 on the server
- add an `if` statement in our FT with a staging URL to test against
```python
staging_server = os.environ.get('STAGING_SERVER')
if staging_server:
    self.live_server_url = 'http://' + staging_server
````
- then we can set up a temporal environment variable to run tests against the server
```bash
STAGING_SERVER=staging.chicocheco.xyz python manage.py test functional_tests
```

## First steps on the server as a non-root user
> Update system, install dependencies, create subfolders, git clone repository as follows (`superlists` stands for the name of the Django project)
```bash
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt update
sudo apt-get install nginx git python3.7 python3.7-venv
export SITENAME=staging.chicocheco.xyz
mkdir -p ~/$SITENAME/database
mkdir -p ~/$SITENAME/static
mkdir -p ~/$SITENAME/virtualenv
git clone https://github.com/chicocheco/tdd_book.git ~/sites/$SITENAME/source
``` 
> Adjust the database location in settings.py to `../database/db.sqlite3` 
and migrate `./virtualenv/bin/python manage.py migrate --noinput`

> Create `requirements.txt` with django only, push and pull to the server

> Create a virtual environment `python3.7 -m venv ~/sites/$SITENAME/virtualenv`

> Install Django in this virtual environment `~/sites/$SITENAME/virtualenv/bin/pip install -r ~/sites/$SITENAME/source/requirements.txt`

> Run Django dev server `~/sites/$SITENAME/virtualenv/bin/python manage.py runserver` (listening on port 8000, locally)

> Create a config file for **nginx** at `/etc/nginx/sites-available/$SITENAME` that will "proxy"
all requests from our domain to the `http://localhost:8000` where it expects to find Django waiting to respond

> Enable the nginx config file (create a symlink) `sudo ln -s /etc/nginx/sites-available/$SITENAME /etc/nginx/sites-enabled/$SITENAME` and remove the default `sudo rm /etc/nginx/sites-enabled/default`

> Reload the nginx web server `sudo systemctl reload nginx` and django dev server

## Production-ready deployment
> Switching to a web server gunicorn from the Django dev server that should be used only for debugging. Install gunicorn `../virtualenv/bin/pip install gunicorn` and 
give gunicorn a path to a WSGI server, which in Django is a function called **application** `~/sites/$SITENAME/virtualenv/bin/gunicorn superlists.wsgi:application`

> Use the nginx server to serve only static files (gunicorn does not do that). Collect all static files 
`../virtualenv/bin/python manage.py collectstatic --noinput` and add `location /static {alias <path>;}` in the nginx 
>config file pointing to the full path of the `static` folder (replace `<path>`)

> Reload nginx and start gunicorn again `~/sites/$SITENAME/virtualenv/bin/gunicorn superlists.wsgi:application`

> Now to be able to serve both staging and live without using 2 different ports (not recommended), use **unix domain sockets** 
and within `location / {}` block add lines `proxy_set_header Host $host;` to make sure that gunicorn and Django know
what domain it is running on (staging, live...) and `proxy_pass http://unix:/tmp/SITENAME.socket;` the unix socket
(previously `proxy_pass http://localhost:8000;`)

> Reload nginx again and now bind the unix socket to gunicorn 
`~/sites/$SITENAME/virtualenv/bin/gunicorn --bind unix:/tmp/SITENAME.socket superlists.wsgi:application`

> Set `DEBUG = False` along with `ALLOWED_HOSTS = ['SITENAME']` but don't commit these changes in git

> Make sure that the gunicorn web server starts automatically on boot or reloads on crash. Place the config file in
`/etc/systemd/system/gunicorn-SITENAME.service` and run the following commands
```bash
sudo systemctl daemon-reload
sudo systemctl enable gunicorn-SITENAME
sudo systemctl start gunicorn-SITENAME
```

> Install gunicorn also locally and add to requirements.txt
```bash
pip install gunicorn
pip freeze | grep gunicorn >> requirements.txt
git commit -am "Add gunicorn to virtualenv requirements"
git push
```

> Put all the previous steps into a fabfile to automate the process. Test it by `cd deploy_tools` on the server and run
`fab deploy:host=<NON-ROOT-USER>@<SITENAME>`. But what we cannot do like this is configuring gunicorn and nginx servers.
For that we can use `sed` ("stream editor") with each template of configuration files. 
We use the `s/replaceme/withthis/g` syntax with `sed`. The `tee` command writes the output both to the screen (stdout)
 and to the file which requires sudo in this case.
 
> Once we have the site live on the server we mark it with these two (2) git tags and push them to the repo. 
```bash
git tag LIVE
export TAG=$(date +DEPLOYED-%d/%m/%y-%H%M) # this generates a timestamp DEPLOYED-11/09/19-0613
echo $TAG # should show "DEPLOYED-" and then the timestamp
git tag $TAG
git push origin LIVE $TAG # pushes the tags up
```