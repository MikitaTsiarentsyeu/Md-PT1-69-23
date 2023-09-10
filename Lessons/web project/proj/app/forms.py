from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class AddPost(forms.Form):

    title = forms.CharField(max_length=100, widget=forms.TextInput())
    content = forms.CharField(widget=forms.Textarea(attrs={'class':"my_text_area"}))
    post_type = forms.ChoiceField(choices=Post.POST_TYPES)
    image = forms.ImageField()

class AddPostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'post_type', 'image')

    def clean_title(self):
        raw_title = self.cleaned_data['title']
        if len(raw_title) > 20:
            raise ValidationError("the title length should be less then 20")
        return raw_title