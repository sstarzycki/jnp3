# -*- coding: utf-8 -*-

from django import forms
from models import Text

class NewTextForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField( \
            widget=forms.Textarea(), \
            label="Content")
