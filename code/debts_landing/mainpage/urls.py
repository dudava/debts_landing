import django.conf
import django.urls
import django.conf.urls.static

from . import views

app_name = "mainpage"

urlpatterns = [
    django.urls.path('', views.MainPageView.as_view(), name="main"),
]

urlpatterns += django.conf.urls.static.static(
    django.conf.settings.MEDIA_URL,
    document_root=django.conf.settings.MEDIA_ROOT,
) if django.conf.settings.DEBUG else []
