from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
from django.contrib.sessions.backends.db import SessionStore
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('email')

    def handle(self, *args, **options):
        session_key = create_pre_authenticated_session(options['email'])
        self.stdout.write(session_key)


def create_pre_authenticated_session(email):
    # session cookies are set for ALL visitors, whether they’re logged in or not
    # client’s session can be simply marked as an authenticated session,
    # and associated with a user ID in its database
    user = User.objects.create(email=email)
    session = SessionStore()
    session[SESSION_KEY] = user.pk  # it's actually the email
    session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
    session.save()
    return session.session_key  # will be added to browser in a cookie
