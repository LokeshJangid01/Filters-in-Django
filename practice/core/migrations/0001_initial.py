# Generated by Django 5.0.4 on 2024-04-06 18:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.FloatField()),
                ('number_in_stock', models.PositiveIntegerField(default=0)),
                ('genre', models.CharField(choices=[('C', 'Crime'), ('N', 'Non Fiction'), ('O', 'Other'), ('S', 'Sci Fi')], max_length=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.author')),
            ],
        ),
    ]
