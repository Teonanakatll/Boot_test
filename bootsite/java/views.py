from django.shortcuts import render

from .models import Chapter

foot = ['icon-youtube-play',
        'icon-paper-plane',
        'icon-vkontakte',
        'icon-instagram',
        'icon-github-circled'
        ]

def index2(request):
    chapt = Chapter.objects.filter(pk__lt=5)
    return render(request, 'java/index2.html', {'foot': foot, 'chapt': chapt})
