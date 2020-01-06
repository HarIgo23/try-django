from django import forms

from .models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    # title = forms.CharField()  # another way to change type of field
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content']
