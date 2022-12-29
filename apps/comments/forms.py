import requests

from django import forms
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

from apps.comments.models import Comment, Circle


class SearchForm(forms.Form):
    query = forms.CharField(
        label=_('Search Profile'), max_length=100, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': _('Field requerid. Search for name, last name or username.'),
            'autofocus': 'autofocus'
        })
    )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['circle', 'comment']

    def send_email(self, form, recipients: list, template_email):
        subject = _('New Feedback Received!')
        message = render_to_string(template_email, {'circle': form.cleaned_data['circle'].name})
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipients)
