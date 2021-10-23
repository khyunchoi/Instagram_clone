from django import forms
from .models import Article, Comment

# class ArticleSelectForm(forms.ModelForm):

#     class Meta:
#         model = Article
#         fields = ('image',)


# class ArticleDetailForm(forms.ModelForm):

#     class Meta:
#         model = Article
#         fields = ('content',)


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('image', 'content',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)