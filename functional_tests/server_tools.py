from fabric.api import run, env
from fabric.context_managers import settings, shell_env

env.key_filename = ['~/standa.pem']  # TODO: remove hardcoded keyfile


def _get_manage_dot_py(host):
    return f'~/sites/{host}/virtualenv/bin/python ~/sites/{host}/manage.py'


def reset_database(host):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f'ubuntu@{host}'):
        run(f'{manage_dot_py} flush --noinput')  # replace for LiveServerTestCase on remote


def _get_server_env_vars(host):
    env_lines = run(f'cat ~/sites/{host}/.env').splitlines()  # get a list
    # create a generator and pass to a dict() constructor
    return dict(line.split('=') for line in env_lines if line)


def create_session_on_server(host, email):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f'ubuntu@{host}'):
        env_vars = _get_server_env_vars(host)
        with shell_env(**env_vars):  # unpack a dict
            session_key = run(f'{manage_dot_py} create_session {email}')
            return session_key.strip()
