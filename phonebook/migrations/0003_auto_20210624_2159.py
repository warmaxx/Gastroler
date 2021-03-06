# Generated by Django 3.2 on 2021-06-24 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20210624_2159'),
        ('phonebook', '0002_alter_status_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='departament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homepage.departament', verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=100, verbose_name='E-mail @rosgvard.ru'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homepage.job', verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='rank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homepage.rank', verbose_name='Звание'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='status',
            field=models.CharField(choices=[(1, 'На службе'), (2, 'Болен'), (3, 'Коммандировка'), (4, 'Отпуск'), (5, 'Декрет'), (6, 'Уволен'), (7, 'Пенсия'), (8, 'Переведен')], max_length=20, verbose_name='Статус'),
        ),
    ]
