from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir contraseña'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'names',
            'last_name',
            'gender',
        )

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales') 

class LoginForm(forms.Form):
    
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                #'style': '{ margin: 10px }',                      '
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        print(self.cleaned_data['username'], self.cleaned_data['password'])
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')

        return  self.cleaned_data

class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña actual'
            }
        )
    )

    password2 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña nueva'
            }
        )
    )

class VerificationForm(forms.Form):
    codregister = forms.CharField(required=True)
    
    def __init__(self, pk, *args, **kwargs):
        self.id_user = pk
        super(VerificationForm, self).__init__(*args, **kwargs)
    
    def clean_codregister(self):
        code = self.cleaned_data['codregister']

        #Validate if the code and id are valids
        if len(code) == 6:
            active = User.objects.cod_validation(
                self.id_user,
                code
            )
            if not active:
                raise forms.ValidationError('El código es incorrecto')
        else:
            raise forms.ValidationError('El código es incorrecto')
    
