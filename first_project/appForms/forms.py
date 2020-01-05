from django import forms
from django.core import validators

class formName(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    verifyEmail = forms.EmailField(label='Re-enter your email :')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    def clean(self):
        allCleanData = super().clean()
        email = allCleanData['email']
        verifyEmail = allCleanData['verifyEmail']
        if email != verifyEmail:
            raise forms.ValidationError("Ensure both emails match")