from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms

class CustomUserCreationForm(UserCreationForm):  # Регистрация
    email = forms.EmailField(required=True)  # Поле для email

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Поля регистрации

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(forms.Form):  # Авторизация
    username_or_email = forms.CharField(label='Имя пользователя или Email', max_length=255)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def clean(self):
        username_or_email = self.cleaned_data.get('username_or_email')
        password = self.cleaned_data.get('password')
        user = None

        # Проверяем, если это email
        if '@' in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
                username_or_email = user.username  # Извлекаем username для аутентификации
            except User.DoesNotExist:
                raise forms.ValidationError('User with this email does not exist.')
        # Если это username
        else:
            user = authenticate(username=username_or_email, password=password)

        # Проверяем пароль и пользователя
        if user is None or not user.check_password(password):
            raise forms.ValidationError('Invalid login credentials.')

        self.cleaned_data['user'] = user
        return self.cleaned_data
