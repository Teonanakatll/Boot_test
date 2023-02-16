from django.shortcuts import render

def index(request):
    about = [
        {'icon': 'icon-list-numbered', 'text': 'Структурированный материал'},
        {'icon': 'icon-rouble', 'text': 'Cимволическая цена'},
        {'icon': 'icon-chart-bar', 'text': 'Пожизненный доступ'},
        {'icon': 'icon-code', 'text': 'Практические задания'},
        {'icon': 'icon-file-video', 'text': '35 видео уроков (5 часов)'},
        {'icon': 'icon-mobile', 'text': 'Просмотр со смартфона'},

    ]
    return render(request, 'boot/index.html', {'about': about})
