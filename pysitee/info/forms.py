from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm, TextInput, DateTimeInput
from .models import Info, CustomUser

class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ['title', 'anons', 'date']
        
        widgets = {
            "title": TextInput(attrs={
                'class': 'form_control',
                'placeholder': 'Name'
            }),
            "anons": TextInput(attrs={
                'class': 'form_control',
                'placeholder': 'Info'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form_control',
                'placeholder': 'Date'
            })
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Username'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'}))
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
        }
        
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'E-mail'}),
        }
    
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email= email).exists():
            raise forms.ValidationError('there is already such an E-mail')
        return email
    
class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled = True , label ='username', widget = forms.TextInput(attrs= {'class':'form-input'}))
    email =  forms.CharField(disabled = True , label ='email', widget = forms.TextInput(attrs= {'class':'form-input'}))  
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'email','first_name', 'last_name']
        
    widgets = {
        'first_name':forms.TextInput(attrs ={'class':'form-input'}),
        'last_name':forms.TextInput(attrs ={'class':'form-input'})
    }  
    
    
class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label ='old password', widget = forms.PasswordInput(attrs= {'class':'form-input'}))
    new_password1 = forms.CharField(label ='new password', widget = forms.PasswordInput(attrs= {'class':'form-input'}))
    new_password2 = forms.CharField(label ='Confirm the password', widget = forms.PasswordInput(attrs= {'class':'form-input'}))
    