# Generated by Django 4.1.6 on 2023-02-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=200, verbose_name='Описание')),
                ('status', models.TextField(max_length=20, verbose_name='Статус')),
                ('execution_date', models.TextField(max_length=10, null=True, verbose_name='Дата исполнения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
            ],
        ),
    ]
