import django.db.models


class Feedback(django.db.models.Model):
    name = django.db.models.CharField('Имя', max_length=100)
    telephone = django.db.models.CharField('Номер телефона', max_length=50)
    
    def __str__(self):
        return f"{self.name}: {self.telephone}"
    