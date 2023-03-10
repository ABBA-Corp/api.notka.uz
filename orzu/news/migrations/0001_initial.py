# Generated by Django 4.0.8 on 2023-01-18 20:27

from django.db import migrations, models
import orzu.news.instances
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', sorl.thumbnail.fields.ImageField(upload_to=orzu.news.instances.get_news_path, verbose_name='Изображение')),
                ('landscape_photo', sorl.thumbnail.fields.ImageField(upload_to='', verbose_name='Альбомное изображение')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_on', models.DateField(auto_now_add=True, verbose_name='Создано')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
