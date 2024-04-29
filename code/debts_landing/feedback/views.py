import django.contrib.messages
import django.views

from . import forms
from . import models


class FeedbackFormView(django.views.View):
    def post(self, request):
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            django.contrib.messages.add_message(request, django.contrib.messages.SUCCESS, 'Ваша заявка успешно создана!')
            form.save()
            print(models.Feedback.objects.all())
        return django.http.HttpResponseRedirect(
            django.urls.reverse('mainpage:main')
        )