import  tempfile
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Profile


class ProfileTestCase(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            first_name='Tester',
            username='tester'
        )
        self.user_two = User.objects.create(
            first_name='Tester 2',
            username='tester_two'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            photo=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            bio='Tester',
            birthday='1997-04-21',
            gender='M',
            cell_phone='(49)98820-0391'
        )
        self.profile_two = Profile.objects.create(
            user=self.user_two,
            photo=tempfile.NamedTemporaryFile(suffix='.jpg').name,
            bio='Tester 2',
            birthday='2000-11-11',
            gender='F',
            cell_phone='(49)99999-9999'
        )

    def test_create_new_profile(self):
        p1 = Profile.objects.get(user__username='tester')
        p2 = Profile.objects.get(user__username='tester_two')
        self.assertEqual(p1.__str__(), self.profile.__str__())
        self.assertEqual(p2.__str__(), self.profile_two.__str__())
