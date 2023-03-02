# Generated by Django 4.1.1 on 2023-03-01 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('java', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'ordering': ['id'], 'verbose_name': 'Глава', 'verbose_name_plural': 'Главы'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['id'], 'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
        migrations.AlterField(
            model_name='chapter',
            name='col',
            field=models.CharField(max_length=100, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Глава'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='text',
            field=models.CharField(max_length=100, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='chap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='java.chapter', verbose_name='Глава'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Название'),
        ),
    ]
