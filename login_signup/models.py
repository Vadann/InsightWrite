from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=150, required=True)
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        required=True,
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput,
        required=True,
    )
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean_username(self):
        # Allow duplicate usernames
        username = self.cleaned_data.get('username')
        return username

    def _post_clean(self):
        super()._post_clean()
        # Remove password validation errors
        if 'password2' in self._errors:
            # Only keep the "passwords don't match" error if it exists
            dont_match_error = [e for e in self._errors['password2'] if 'password' in e and 'match' in e]
            if dont_match_error:
                self._errors['password2'] = dont_match_error
            else:
                del self._errors['password2']

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        # Remove the _1 suffix - just use the username as provided
        user.username = self.cleaned_data["username"]
        if commit:
            user.save()
        return user

