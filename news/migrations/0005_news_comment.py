# Generated by Django 3.2 on 2021-06-20 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Комментарий'),
        ),
    ]
