import django.forms

from . import models


class FeedbackForm(django.forms.ModelForm):
    class Meta:
        model = models.Feedback
        fields = ('name', 'telephone')
        widgets = {
            'name': django.forms.TextInput(attrs={'placeholder': 'Имя'}),
            'telephone': django.forms.TextInput(attrs={'placeholder': 'Телефон'}),
        }