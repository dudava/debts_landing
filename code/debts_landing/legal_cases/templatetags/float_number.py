import django.template

register = django.template.Library()


@register.filter(name='with_spaces')
def with_spaces(number):
    str_number = str(number)
    integer_part = str_number[:str_number.find('.')]
    fract_part = str_number[str_number.find('.') + 1:]
    integer_part = ' '.join(integer_part[_: _ + 3] for _ in range(0, len(integer_part), 3))
    return f'{integer_part},{fract_part}'
