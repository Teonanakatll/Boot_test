from django.db import models

class Chapter(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Глава')
    text = models.CharField(max_length=100, verbose_name='Описание')
    col = models.CharField(max_length=100, verbose_name='Количество')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'
        ordering = ['id']

class Lesson(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    chap = models.ForeignKey('Chapter', on_delete=models.CASCADE, verbose_name='Глава')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['id']
