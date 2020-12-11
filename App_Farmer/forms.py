
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import Post  #Profile
from django.forms import forms

'''''
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic',)


class FarmerSignUpForm(UserCreationForm):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'password1', 'password2',)

'''''


class PostForm(forms):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'image', ]
        
