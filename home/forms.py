from django import forms

from blog.forms import BootstrapFormMixin
from home.models import Comment


class BookAddForm(forms.ModelForm, BootstrapFormMixin):

    class Meta:
        model = Comment
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super(BookAddForm, self). __init__(*args, **kwargs)
        BootstrapFormMixin.__init__(self)
