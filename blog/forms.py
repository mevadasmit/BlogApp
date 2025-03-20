from django import forms
from .models import PostImage , BlogComment

class PostImagesForm(forms.ModelForm):
        class Meta:
            model = PostImage
            fields = ['image']


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['comment']

