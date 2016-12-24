# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-12-24 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fias', '0014_addrobj_plancode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addrobj',
            name='ifnsfl',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код ИФНС ФЗ'),
        ),
        migrations.AlterField(
            model_name='addrobj',
            name='ifnsul',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код ИФНС ЮЛ'),
        ),
        migrations.AlterField(
            model_name='addrobj',
            name='okato',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='ОКАТО'),
        ),
        migrations.AlterField(
            model_name='addrobj',
            name='oktmo',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='ОКТМО'),
        ),
        migrations.AlterField(
            model_name='addrobj',
            name='postalcode',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Почтовый индекс'),
        ),
        migrations.AlterField(
            model_name='addrobj',
            name='terrifnsfl',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код территориального участка ИФНС ФЛ'),
        ),
        migrations.AlterField(
            model_name='addrobj',
            name='terrifnsul',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код территориального участка ИФНС ЮЛ'),
        ),
        migrations.AlterField(
            model_name='house',
            name='ifnsfl',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код ИФНС ФЗ'),
        ),
        migrations.AlterField(
            model_name='house',
            name='ifnsul',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код ИФНС ЮЛ'),
        ),
        migrations.AlterField(
            model_name='house',
            name='okato',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='ОКАТО'),
        ),
        migrations.AlterField(
            model_name='house',
            name='oktmo',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='ОКТМО'),
        ),
        migrations.AlterField(
            model_name='house',
            name='postalcode',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Почтовый индекс'),
        ),
        migrations.AlterField(
            model_name='house',
            name='terrifnsfl',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код территориального участка ИФНС ФЛ'),
        ),
        migrations.AlterField(
            model_name='house',
            name='terrifnsul',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код территориального участка ИФНС ЮЛ'),
        ),
        migrations.AlterField(
            model_name='houseint',
            name='ifnsfl',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код ИФНС ФЗ'),
        ),
        migrations.AlterField(
            model_name='houseint',
            name='ifnsul',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код ИФНС ЮЛ'),
        ),
        migrations.AlterField(
            model_name='houseint',
            name='okato',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='ОКАТО'),
        ),
        migrations.AlterField(
            model_name='houseint',
            name='oktmo',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='ОКТМО'),
        ),
        migrations.AlterField(
            model_name='houseint',
            name='postalcode',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Почтовый индекс'),
        ),
        migrations.AlterField(
            model_name='houseint',
            name='terrifnsfl',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код территориального участка ИФНС ФЛ'),
        ),
        migrations.AlterField(
            model_name='houseint',
            name='terrifnsul',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код территориального участка ИФНС ЮЛ'),
        ),
        migrations.AlterField(
            model_name='landmark',
            name='ifnsfl',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код ИФНС ФЗ'),
        ),
        migrations.AlterField(
            model_name='landmark',
            name='ifnsul',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код ИФНС ЮЛ'),
        ),
        migrations.AlterField(
            model_name='landmark',
            name='okato',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='ОКАТО'),
        ),
        migrations.AlterField(
            model_name='landmark',
            name='oktmo',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='ОКТМО'),
        ),
        migrations.AlterField(
            model_name='landmark',
            name='postalcode',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Почтовый индекс'),
        ),
        migrations.AlterField(
            model_name='landmark',
            name='terrifnsfl',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код территориального участка ИФНС ФЛ'),
        ),
        migrations.AlterField(
            model_name='landmark',
            name='terrifnsul',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код территориального участка ИФНС ЮЛ'),
        ),
        migrations.AlterField(
            model_name='stead',
            name='ifnsfl',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код ИФНС ФЗ'),
        ),
        migrations.AlterField(
            model_name='stead',
            name='ifnsul',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код ИФНС ЮЛ'),
        ),
        migrations.AlterField(
            model_name='stead',
            name='okato',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='ОКАТО'),
        ),
        migrations.AlterField(
            model_name='stead',
            name='oktmo',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='ОКТМО'),
        ),
        migrations.AlterField(
            model_name='stead',
            name='postalcode',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Почтовый индекс'),
        ),
        migrations.AlterField(
            model_name='stead',
            name='terrifnsfl',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код территориального участка ИФНС ФЛ'),
        ),
        migrations.AlterField(
            model_name='stead',
            name='terrifnsul',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Код территориального участка ИФНС ЮЛ'),
        ),
    ]
