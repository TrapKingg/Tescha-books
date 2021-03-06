from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Retype-password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password Didnt match')
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Este email ya esta en uso')
        return data

class UserForm(forms.ModelForm):
    first_name = forms.CharField(label="Nombre(s)", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Apellidos", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="E-mail", widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    matricula = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pic = forms.ImageField(label="Foto de Perfil")
    class Meta:
        model = Profile
        fields = ['degree', 'matricula', 'pic', 'semestre']

    # def clean_matricula(self):
    #     data = self.cleaned_data['matricula']
    #     if User.objects.filter(matricula=data).exists():
    #         raise forms.ValidationError('Ya existe un usuario registrado con esta matricula.')
    #     return data
