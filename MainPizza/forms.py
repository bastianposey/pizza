from django import forms
from .models import Comment, Pizza, Topping


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text':''}