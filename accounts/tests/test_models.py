from django.test import TestCase
from django.contrib.auth import get_user_model

from accounts.models import Token

User = get_user_model()

"""
Driving Django models with basic TDD involves jumping through a few hoops because of the migration, 
so we’ll see a few iterations like this—minimal code change, make migrations, get new error, delete migrations, 
re-create new migrations, another code change, and so on...

Note that for testing we are just fine with running `makemigration` and not `migrate`.
https://stackoverflow.com/questions/50178120/django-development-server-using-testcase-database

Before de-spiking (checkout back to master) that consisted of migrating the DB (messing around with models), 
we must first migrate back using the previous migration file to go back because git does not do that on its own.
python manage.py migrate <00XY>
"""


class UserModelTest(TestCase):

    @staticmethod
    def test_user_is_valid_with_email_only():
        user = User(email='a@b.com')
        user.full_clean()  # should not raise

    def test_email_is_primary_key(self):
        # test as documentation - we use email directly as a primary key (it must be unique)
        user = User(email='a@b.com')
        self.assertEqual(user.pk, 'a@b.com')


class TokenModelTest(TestCase):

    def test_links_user_with_auto_generated_uid(self):
        token1 = Token.objects.create(email='a@b.com')
        token2 = Token.objects.create(email='a@b.com')
        self.assertNotEqual(token1.uid, token2.uid)
