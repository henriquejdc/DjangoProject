from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class ProfileManager(models.Manager):

    def search(self, query):
        qs = self.get_queryset()
        if query:
            or_lookup = (
                Q(user__first_name=query) | Q(user__last_name=query) | Q(user__username__icontains=query)
            )
            qs = qs.filter(or_lookup)
            print(qs)
        return qs


class Profile(models.Model):
    CHOICES_GENDERS = (('M', _('Male')), ('F', _('Female')))

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))
    photo = models.ImageField(_('Photo'), upload_to='photos')
    bio = models.TextField(_('Biography'), blank=True, null=True)
    birthday = models.DateField(_('Birthday'), blank=True, null=True)
    gender = models.CharField(
        _('Gender'),
        max_length=1,
        choices=CHOICES_GENDERS,
        blank=True,
        null=True
    )
    cell_phone = models.CharField(_('Cellphone'), max_length=14, blank=True)

    objects = ProfileManager()

    class Meta:
        ordering = ['id']
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return "{} - {}".format(self.pk, self.user.username)
