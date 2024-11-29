from .models import Bb, Rubric
from django.forms import ModelForm


class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')

