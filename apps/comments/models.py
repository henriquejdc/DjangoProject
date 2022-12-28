from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Circle(models.Model):
    name = models.CharField(_('Name'), max_length=50)

    class Meta:
        ordering = ['id']
        verbose_name = _('Circle')
        verbose_name_plural = _('Circles')

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))
    circle = models.ForeignKey(Circle, on_delete=models.CASCADE, verbose_name=_('Circle'))
    comment = models.TextField(_('Comment'))
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(_('Read'), default=False)

    class Meta:
        ordering = ['id']
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return '{} - {}: {}'.format(self.user.username, self.created_at.date(), self.comment)
