Provisioning a new site
=======================

## Required packages:
* nginx
* Python 3.7
* virtualenv + pip
* git

eg, on Ubuntu:
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get install nginx git python3.7 python3.7-venv
```
    
## Nginx Virtual Host config
* see nginx.template.conf
* replace DOMAIN with, e.g., chicocheco.xyz using `sed` and `sudo tee` and enable a conf file by sym-linking it 
```bash
sed "s/DOMAIN/chicocheco.xyz/g" source/deploy_tools/nginx.template.conf | sudo tee /etc/nginx/sites-available/chicocheco.xyz
sudo ln -s ../sites-available/chicocheco.xyz /etc/nginx/sites-enabled/chicocheco.xyz
sudo systemctl reload nginx
```

## Systemd service
* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., chicocheco.xyz with `sed` and `sudo tee`
```bash
sed "s/DOMAIN/chicocheco.xyz/g" source/deploy_tools/gunicorn-systemd.template.service | sudo tee /etc/systemd/system/gunicorn-chicocheco.xyz.service
sudo systemctl daemon-reload
sudo systemctl enable gunicorn-chicocheco.xyz
sudo systemctl start gunicorn-chicocheco.xyz
```

## Folder structure
Assume we have a user account at /home/username
```
/home/username
└── sites
    ├── DOMAIN1
    │    ├── .env
    │    ├── db.sqlite3
    │    ├── manage.py etc
    │    ├── static
    │    └── virtualenv
    └── DOMAIN2
         ├── .env
         ├── db.sqlite3
         ├── etc
```