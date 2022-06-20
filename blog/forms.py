from dataclasses import fields
from unicodedata import category
from django import forms
from .models import Comment, Category, Tag
from django.contrib.auth import get_user_model

user = get_user_model

class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'text',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'textarea'})
        }

class PostSearchForm(forms.Form):
    key_word = forms.CharField(
        label='キーワード', required=False,
        widget=forms.TextInput(attrs={'class': 'input'})
    )
    category = forms.ModelChoiceField(
        label='カテゴリの選択', required=False,
        queryset=Category.objects.all(),
    )
    tags = forms.ModelMultipleChoiceField(
        label='タグの選択', required=False,
        queryset=Tag.objects.all(),
    )