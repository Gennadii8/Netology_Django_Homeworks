from datetime import datetime
from django import template


register = template.Library()


@register.filter
def format_date(value):
    minutes_gone = (datetime.timestamp(datetime.now()) - value) / 60
    hours_gone = round(minutes_gone / 60)
    if minutes_gone < 10:
        return 'только что'
    if (hours_gone < 24) and (hours_gone > 0):
        if hours_gone in [1, 21]:
            return f'{hours_gone} час назад'
        if hours_gone in [2, 3, 4, 22, 23]:
            return f'{hours_gone} часа назад'
        return f'{hours_gone} часов назад'
    else:
        return datetime.fromtimestamp(value).date().strftime("%Y-%m-%d")


@register.filter
def score(value):
    if value < -5:
        value = 'все плохо'
    elif -5 <= value <= 5:
        value = 'нейтрально'
    elif value > 5:
        value = 'хорошо'
    else:
        pass
    return value


@register.filter
def format_num_comments(value):
    if value == 0:
        value = 'Оставьте комментарий'
    elif 0 < value <= 50:
        pass
    elif value > 50:
        value = '50+'
    return value


@register.filter
def format_selftext(value, count=5):
    final_list = []
    if value:
        word_list = value.split()
        if len(word_list) > (count * 2):
            for i in range(count):
                final_list.append(word_list[i])
            final_list.append('...')
            for i in range(len(word_list) - count, len(word_list), 1):
                final_list.append(word_list[i])
            final_str = ' '.join(final_list)
            return final_str
    else:
        return value


