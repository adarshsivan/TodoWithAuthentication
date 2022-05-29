# Generated by Django 4.0.4 on 2022-05-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
