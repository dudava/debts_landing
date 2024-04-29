import django.contrib.admin

from . import models


@django.contrib.admin.register(models.LegalCase)
class CaseAdmin(django.contrib.admin.ModelAdmin):
    pass
