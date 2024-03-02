# Generated by Django 4.2.5 on 2024-02-24 21:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafedra', '0011_alter_infopage_ingo_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeepage',
            name='page_name',
            field=models.CharField(default='Название', max_length=20, verbose_name='Название страницы'),
        ),
        migrations.AddField(
            model_name='filepage',
            name='page_name',
            field=models.CharField(default='Название', max_length=20, verbose_name='Название страницы'),
        ),
        migrations.AddField(
            model_name='infopage',
            name='page_name',
            field=models.CharField(default='Название', max_length=20, verbose_name='Название страницы'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='pdf_file',
            field=models.FileField(upload_to='static/cafe+dra/pdfs/', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]
