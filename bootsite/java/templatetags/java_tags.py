from django import template

from java.models import Lesson

register = template.Library()

about_list = [
    {'icon': 'icon-list-numbered', 'title': 'Структурированный материал',
     'text': 'Грамотно составленные уроки с наглядными практическими примерами способствуют'
             ' лучшему усвоению материала.'},
    {'icon': 'icon-rouble', 'title': 'Платформа для обучения',
     'text': 'Обучение проходит на платформе Stepik. На Stepik вы можете приобрести курс по'
             ' выгодной цене и получить сертификат.'},
    {'icon': 'icon-chart-line', 'title': 'Пожизненный доступ',
     'text': 'Курс предоставляется вам навсегда, без каких-либо лимитов и ограничений по'
             ' времени. Занимайтесь тогда, когда вам удобно.'},
    {'icon': 'icon-code', 'title': 'Практические задания',
     'text': 'По завершении курса у вас будет опыт создания множества современных интерактивных'
             ' элементов для сайта'},
    {'icon': 'icon-upload-cloud-outline', 'title': 'Огромный обьем информации',
     'text': 'Видеокурс включает в себя 65 уроков общей продолжительностью 20 часов и 114 готовых'
             ' примеров кода.'},
    {'icon': 'icon-group', 'title': 'Поддержка от автора',
     'text': 'Вы будете получать необходимую обратную связь от автора курса. Вопросы можно задавать'
             ' на платформе Stepik.'},

]

@register.simple_tag(name='about')
def get_about():
    return about_list

@register.simple_tag(name='lessons')
def show_lessons(filter=None):
    return Lesson.objects.filter(chap=filter)

