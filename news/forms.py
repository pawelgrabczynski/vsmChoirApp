from django.forms import ModelForm
from django import forms
from .models import News

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'short_description','body', 'featured_image','link']

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})  