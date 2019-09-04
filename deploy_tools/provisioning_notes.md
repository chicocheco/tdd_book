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
* replace SITENAME with, e.g., chicocheco.xyz

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., chicocheco.xyz

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