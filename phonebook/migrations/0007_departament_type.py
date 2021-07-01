# Generated by Django 3.2 on 2021-06-24 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0006_alter_contact_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='departament',
            name='type',
            field=models.IntegerField(choices=[(1, 'Отдел'), (2, 'Округ')], default=1, verbose_name='Тип подразделения'),
            preserve_default=False,
        ),
    ]
