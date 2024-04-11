# Generated by Django 5.0.1 on 2024-01-30 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Radio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='OpRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolename', models.CharField(max_length=40, verbose_name='Rooli')),
                ('radionick', models.CharField(blank=True, max_length=20, verbose_name='Radiokutsu')),
                ('players', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='communities.member', verbose_name='Pelaaja')),
                ('radio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='events.radio', verbose_name='Radio')),
            ],
        ),
        migrations.CreateModel(
            name='OpRoleBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Yksikkö')),
                ('oprole', models.ManyToManyField(blank=True, to='events.oprole', verbose_name='Roolit')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.BooleanField(verbose_name='Julkaistu')),
                ('op_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Operaation nimi')),
                ('op_map', models.CharField(blank=True, max_length=40, null=True, verbose_name='Kartan nimi')),
                ('op_startdatetime', models.DateTimeField(blank=True, null=True, verbose_name='Tehtävän aloitus')),
                ('op_duration', models.TimeField(blank=True, null=True, verbose_name='Tehtävän kesto')),
                ('op_slotopendatetime', models.DateTimeField(blank=True, null=True, verbose_name='Slottaus aukeaa')),
                ('plandatetime', models.DateTimeField(blank=True, null=True, verbose_name='Suunnittelun aloitus')),
                ('planduration', models.TimeField(blank=True, null=True, verbose_name='Suunnittelun kesto')),
                ('op_modpreset', models.TextField(blank=True, null=True, verbose_name='Modpreset')),
                ('server_a3address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Arma3 palvelin')),
                ('server_a3port', models.CharField(blank=True, max_length=100, null=True, verbose_name='Arma3 portti')),
                ('server_a3pwd', models.CharField(blank=True, max_length=100, null=True, verbose_name='Arma3 salasana')),
                ('server_tsaddress', models.CharField(blank=True, max_length=100, null=True, verbose_name='TeamSpeak palvelin')),
                ('server_tsport', models.CharField(blank=True, max_length=100, null=True, verbose_name='TeamSpeak portti')),
                ('server_tspwd', models.CharField(blank=True, max_length=100, null=True, verbose_name='TeamSpeak salasana')),
                ('op_slottingstartdatetime', models.DateTimeField(blank=True, null=True, verbose_name='Slottaus aukeaa')),
                ('op_slottingcheckdatetime', models.DateTimeField(blank=True, null=True, verbose_name='Slottaus tarkastus')),
                ('op_minplayers', models.IntegerField(blank=True, null=True, verbose_name='Pelaajamäärä minimi')),
                ('op_maxplayers', models.IntegerField(blank=True, null=True, verbose_name='Pelaajamäärä maksimi')),
                ('op_spec_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Tehtävän ajankohta')),
                ('op_spec_weather', models.TextField(blank=True, null=True, verbose_name='Sää')),
                ('op_rules', models.TextField(blank=True, null=True, verbose_name='Säännöt')),
                ('op_situation', models.TextField(blank=True, null=True, verbose_name='Tilanne')),
                ('op_spec_friedlies', models.TextField(blank=True, null=True, verbose_name='Omat joukot')),
                ('op_spec_enemies', models.TextField(blank=True, null=True, verbose_name='Viholliset')),
                ('op_spec_civilians', models.TextField(blank=True, null=True, verbose_name='Siviilit')),
                ('op_spec_roe', models.TextField(blank=True, null=True, verbose_name='Tulenavaussäännöt')),
                ('op_spec_assets', models.TextField(blank=True, null=True, verbose_name='Oma kalusto')),
                ('op_spec_mission', models.TextField(blank=True, null=True, verbose_name='Tehtävä')),
                ('op_spec_proceeding', models.TextField(blank=True, null=True, verbose_name='Toteutus')),
                ('op_spec_supports', models.TextField(blank=True, null=True, verbose_name='Huolto')),
                ('op_spec_comms', models.TextField(blank=True, null=True, verbose_name='Johto ja viestintä')),
                ('op_organizer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='communities.community', verbose_name='Järjestäjä')),
                ('op_rolebox', models.ManyToManyField(blank=True, to='events.oprolebox', verbose_name='Yksikkö')),
            ],
        ),
    ]