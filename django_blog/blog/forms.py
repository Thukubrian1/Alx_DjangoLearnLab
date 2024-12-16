from django import forms
from .models import Comment, Post, Tag
from taggit.forms import TagWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Add a comment...'}),
        }

class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=TagWidget(), required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        tags = self.cleaned_data['tags']
        if commit:
            instance.save()
            instance.tags.clear()
            for tag_name in tags.split(','):
                tag, _ = Tag.objects.get_or_create(name=tag_name.strip())
                instance.tags.add(tag)
        return instance
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']