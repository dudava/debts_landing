import django.urls

from . import views

app_name = 'feedback'

urlpatterns = [
    django.urls.path('', views.FeedbackFormView.as_view(), name='form'),
]
