# Generated by Django 5.0.1 on 2024-01-31 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Lisätty')),
                ('new', models.TextField(verbose_name='Sisältö')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='communities.member', verbose_name='Lisääjä')),
            ],
        ),
    ]
