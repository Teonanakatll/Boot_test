from django.urls import path

from .views import index2

urlpatterns = [
    path('', index2, name='java')
]