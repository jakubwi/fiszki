# Generated by Django 2.1.1 on 2018-09-17 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0002_auto_20180917_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
