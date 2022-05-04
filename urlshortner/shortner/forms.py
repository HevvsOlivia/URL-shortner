from django import forms
from .models import Link

class NewLinkForm(forms.ModelForm):
    original = forms.URLField()

    class Meta:
        model = Link
        fields = ['original']
