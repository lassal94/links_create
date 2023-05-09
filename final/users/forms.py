from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        del self.fields['password2']

    username = forms.CharField(label='Имя пользователя',
                               required=True,
                               help_text=mark_safe('''<ul class="helps">
                                                        <li>Обязательное поле. Не более 150 символов.</li>
                                                        <li>Только буквы, цифры и символы @/,/+/-/_</li>
                                                    </ul>'''),
                               max_length=150,
                               widget=forms.TextInput(
                               attrs={'class': 'form-control'}))

    email = forms.EmailField(label='Email',
                             required=True,
                             widget=forms.TextInput(
                             attrs={'class': 'form-control', 'placeholder': 'Введите адрес эл. почты'}))

    password1 = forms.CharField(label='Пароль',
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                min_length=8,
                                help_text=mark_safe('''<ul class="helps">
                                                        <li>Ваш пароль не должен совпадать с вашим именем</li>
                                                        <li>Ваш пароль должен содержать как минимум 8 символов</li>
                                                        <li>Ваш пароль не должен быть одним из широко распространенных</li>
                                                        <li>Ваш пароль не может состоять только из цифр</li>
                                                    </ul>'''))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя',
                               required=False,
                               help_text=mark_safe('''<ul class="helps">
                                                        <li>Обязательное поле. Не более 150 символов.</li>
                                                        <li>Только буквы, цифры и символы @/,/+/-/_</li>
                                                    </ul>'''),
                               max_length=150,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control'}))

    email = forms.EmailField(label='Email',
                             required=False,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': 'Введите адрес эл. почты'}))

    class Meta:
        model = User
        fields = ['username', 'email']