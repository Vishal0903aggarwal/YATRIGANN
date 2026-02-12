from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # This loop removes the help text and adds Bootstrap styling
        for field in self.fields:
            self.fields[field].help_text = "" 
            self.fields[field].widget.attrs.update({'class': 'form-control', 'placeholder': f'Enter {field}'})