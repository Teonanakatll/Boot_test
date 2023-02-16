from django.shortcuts import render

about = [
        {'icon': 'icon-list-numbered', 'text': 'Структурированный материал'},
        {'icon': 'icon-rouble', 'text': 'Cимволическая цена'},
        {'icon': 'icon-chart-bar', 'text': 'Пожизненный доступ'},
        {'icon': 'icon-code', 'text': 'Практические задания'},
        {'icon': 'icon-file-video', 'text': '35 видео уроков (5 часов)'},
        {'icon': 'icon-mobile', 'text': 'Просмотр со смартфона'},
    ]
forwhom = [
    {'text': 'Хочет научиться создавать сайты своими силами'},
    {'text': 'Учится современным инструментам разработки'},
    {'text': 'Ещё не знает язык HTML и CSS, но хочет выучить'},
    {'text': 'Хочет стать крутым мастером и зарабатывать деньги'},
]
def index(request):
    return render(request, 'boot/index.html', {'about': about, 'whom': forwhom})
