from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    # the Form class is not dynamic. It's basic, and does not
    # link to a model.

    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    # ModelForm class links to a model. You cn save data from this form straight to database
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
