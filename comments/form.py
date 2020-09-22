from django import forms
from django.forms import widgets


class PostComment(forms.Form):
    comment_text = forms.CharField(label="",widget = widgets.TextInput())
