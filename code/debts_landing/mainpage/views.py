import django.contrib.messages
import django.http
import django.views
import django.shortcuts
import django.urls
import django.views.generic.edit

from feedback import forms
import legal_cases.models


class MainPageView(django.views.View):
    def get(self, request):
        template_name = "mainpage/index.html"
        first_5_cases = legal_cases.models.LegalCase.objects.order_by('-id')[:5]
        context = {
            'form': forms.FeedbackForm(),
            'cases': first_5_cases,
        }
        return django.shortcuts.render(request, template_name, context)