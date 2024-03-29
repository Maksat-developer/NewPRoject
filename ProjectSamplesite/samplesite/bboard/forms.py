from django.forms import ModelForm

from .models import Bboard, Rubric


class BboardForm(ModelForm):
    class Meta:
        model = Bboard
        fields = ('title', 'content', 'price', 'rubric')


    