from django import forms
from django.utils.translation import gettext_lazy as _

from apps.comments.models import Comment


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
