from django import forms


class MethodSelectionForm(forms.Form):
    PARSE_METHOD_CHOICES = [
        ("requests", 'Requests and Bs4'),
        ("Selenium", "Selenium"),
	]
    method = forms.ChoiceField(choices=PARSE_METHOD_CHOICES)



class ParsingForm(forms.Form):
    url = forms.URLField(label="link on site", widget=forms.URLInput(attrs={'placeholder': 'https://example.com'}))
    selector = forms.CharField(label='CSS selector', help_text='img.my-image-classes')


