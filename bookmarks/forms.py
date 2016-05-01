from django import forms
from django.contrib.auth.models import User
import re


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if re.search(r"^\w+$", username):
            if not User.objects.filter(username=username):
                return username
            else:
                raise forms.ValidationError('username already exists')
        else:
            raise forms.ValidationError('username can only contain alphnumeric characters and underscore')

    def clean_repeat_password(self):
        if 'password' in self.cleaned_data:
            repeat_password = self.cleaned_data['repeat_password']
            if repeat_password == self.cleaned_data['password']:
                return repeat_password
            else:
                raise forms.ValidationError("passwords don't match")

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) >= 10:
            if not password.isalpha():
                if not password.isdigit():
                    return password
                else:
                    raise forms.ValidationError('password must contain 1 letter')
            else:
                raise forms.ValidationError('password must contain at least 1 digit')
        else:
            raise forms.ValidationError('password must be 10 characters or longer')


class BookmarkForm(forms.Form):
    title = forms.CharField(max_length=200)
    url = forms.URLField(widget=forms.TextInput)
    tags = forms.CharField(required=False, widget=forms.TextInput)
    share = forms.BooleanField(label='share on the main page', required=False)


class SearchForm(forms.Form):
    query = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'size': 32}),
                            label='Enter a keyword to search for'
                            )
