Provisioning a new site
=======================

## Required packages:
* nginx
* Python 3.7
* virtualenv + pip
* git

eg, on Ubuntu:

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get install nginx git python3.7 python3.7-venv
    
## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., chicocheco.xyz using `sed` and `sudo tee` and enable a conf file by sym-linking it 

```bash
sed "s/SITENAME/superlists.ottg.eu/g" source/deploy_tools/nginx.template.conf | sudo tee /etc/nginx/sites-available/superlists.ottg.eu
sudo ln -s ../sites-available/superlists.ottg.eu /etc/nginx/sites-enabled/superlists.ottg.eu
```

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., chicocheco.xyz with `sed` and `sudo tee`

```bash
sed "s/SITENAME/superlists.ottg.eu/g" source/deploy_tools/gunicorn-systemd.template.service | sudo tee /etc/systemd/system/gunicorn-superlists.ottg.eu.service
```

## Folder structure
Assume we have a user account at /home/username
```/home/username
└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv
```