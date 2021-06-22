from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "username", "email")


# from django import forms

# from .models import Comment, Post


# class PostForm(forms.ModelForm):

#     class Meta:
#         model = Post
#         fields = ('text', 'group', 'image')


# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         fields = ('text',)
#         widgets = {
#             'text': forms.Textarea()
#         }
