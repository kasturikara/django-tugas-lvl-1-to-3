from django import forms
from django.core import validators


def check_for_a(value):
    if value[0].lower() != "a":
        raise forms.ValidationError("NAME NEEDS TO START WITH A")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_a])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again:")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data["email"]
        vmail = all_clean_data["verify_email"]

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")
