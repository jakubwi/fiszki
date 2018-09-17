# Generated by Django 2.1.1 on 2018-09-17 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0002_deck_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('front', models.TextField()),
                ('back', models.TextField()),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decks.Deck')),
            ],
        ),
    ]
