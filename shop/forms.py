from django import forms
import re

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form__input'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if username is None:
            raise forms.ValidationError("Username not found.")
        return username

    def clean_password(self):
        password = self.cleaned_data['password']

        if re.fullmatch(r'[A-Z][a-z][0-9]{8}', password) is None:
            raise forms.ValidationError("Password not valid.")
        return password

class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form__input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form__input'}))
    reset_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form__input'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username is None:
            raise forms.ValidationError("Username not found.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        reset_password = self.cleaned_data.get('reset_password')
        if re.fullmatch(r'[A-Z][a-z][0-9]{8}', password) is None:
            if password != reset_password:
                raise forms.ValidationError("Password not valid.")

        return password


