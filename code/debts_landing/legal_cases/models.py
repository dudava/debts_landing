import django.db.models
import django.core.validators


class LegalCase(django.db.models.Model):
    number = django.db.models.CharField('Номер дела', max_length=30)
    city = django.db.models.CharField('Город', max_length=30)
    amount_debt = django.db.models.FloatField(
        'Сумма долга',
        validators=[django.core.validators.MinValueValidator(0), ],
    )
    writenoff_debt = django.db.models.FloatField(
        'Списано долга', 
        validators=[django.core.validators.MinValueValidator(0), ],
    )
    number_credits = django.db.models.PositiveSmallIntegerField('Кредитов')
    date_start_work = django.db.models.DateField('Начало работы')
    date_case_filed = django.db.models.DateField('Подано')
    date_declared_bankrupt = django.db.models.DateField('Признана банкротом')
    date_case_completed = django.db.models.DateField('Завершено')
    case_pdf = django.db.models.FileField('PDF файл дела', upload_to='cases_pdf')

    def __str__(self):
        return f'Дело № {self.number}'

    class Meta:
        verbose_name = 'Дело'
        verbose_name_plural = 'Дела'
