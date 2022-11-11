import  tempfile
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Circle, Comment


class ProfileTestCase(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            first_name='Tester',
            username='tester'
        )
        self.circle = Circle.objects.create(name='Friends')
        self.comment = Comment.objects.create(
            user=self.user,
            circle=self.circle,
            comment='Hello world',
        )

    def test_create_new_comment(self):
        comment = Comment.objects.get(user=self.user)
        self.assertEqual(comment.__str__(), self.comment.__str__())
