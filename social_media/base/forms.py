from .models import Profile, Post, Comment
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

# Форма для редактирования профиля пользователя
class EditProfileNewForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'description', 'profileimg')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

# Форма для профиля пользователя на странице профиля
class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'description', 'profileimg')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

# Форма для создания поста
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'caption', 'location', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Теги'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'caption': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Местоположение'}),
        }

# Форма для изменения пароля
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

# Форма для комментариев
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

# Форма для редактирования поста
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'caption', 'location', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Теги'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}),
            'caption': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Местоположение'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }