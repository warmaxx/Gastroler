# Generated by Django 3.2 on 2021-06-20 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210620_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='title',
            field=models.CharField(default=1, max_length=200, verbose_name='Заголовок'),
            preserve_default=False,
        ),
    ]
