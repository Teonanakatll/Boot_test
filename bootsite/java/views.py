from django.shortcuts import render

from .models import Chapter


def index2(request):
    chapt = Chapter.objects.filter(pk__lt=5)
    return render(request, 'java/index2.html', {'chapt': chapt})
