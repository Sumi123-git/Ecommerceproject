# Generated by Django 3.2.11 on 2022-01-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['date_added']},
        ),
        migrations.AlterField(
            model_name='cart',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]
