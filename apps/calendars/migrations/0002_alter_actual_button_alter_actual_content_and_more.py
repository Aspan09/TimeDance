# Generated by Django 4.2 on 2023-06-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actual',
            name='button',
            field=models.CharField(blank=True, max_length=100, verbose_name='Schaltfläche'),
        ),
        migrations.AlterField(
            model_name='actual',
            name='content',
            field=models.TextField(max_length=500, verbose_name='Inhalt'),
        ),
        migrations.AlterField(
            model_name='actual',
            name='image',
            field=models.ImageField(blank=True, upload_to='resource', verbose_name='Fotos aktuell'),
        ),
        migrations.AlterField(
            model_name='actual',
            name='link',
            field=models.CharField(blank=True, max_length=300, verbose_name='Der Link'),
        ),
        migrations.AlterField(
            model_name='actual',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Vergaldungen'),
        ),
        migrations.AlterField(
            model_name='friday',
            name='numbers',
            field=models.CharField(blank=True, verbose_name='Zahl'),
        ),
        migrations.AlterField(
            model_name='friday',
            name='time',
            field=models.CharField(blank=True, verbose_name='Zeit'),
        ),
        migrations.AlterField(
            model_name='monday',
            name='numbers',
            field=models.CharField(blank=True, verbose_name='Zahl'),
        ),
        migrations.AlterField(
            model_name='monday',
            name='time',
            field=models.CharField(blank=True, verbose_name='Zeit'),
        ),
        migrations.AlterField(
            model_name='saturday',
            name='numbers',
            field=models.CharField(blank=True, verbose_name='Zahl'),
        ),
        migrations.AlterField(
            model_name='saturday',
            name='time',
            field=models.CharField(blank=True, verbose_name='Zeit'),
        ),
        migrations.AlterField(
            model_name='sunday',
            name='numbers',
            field=models.CharField(blank=True, verbose_name='Zahl'),
        ),
        migrations.AlterField(
            model_name='sunday',
            name='time',
            field=models.CharField(blank=True, verbose_name='Zeit'),
        ),
        migrations.AlterField(
            model_name='thursday',
            name='numbers',
            field=models.CharField(blank=True, verbose_name='Zahl'),
        ),
        migrations.AlterField(
            model_name='thursday',
            name='time',
            field=models.CharField(blank=True, verbose_name='Zeit'),
        ),
        migrations.AlterField(
            model_name='tuesday',
            name='numbers',
            field=models.CharField(blank=True, verbose_name='Zahl'),
        ),
        migrations.AlterField(
            model_name='tuesday',
            name='time',
            field=models.CharField(blank=True, verbose_name='Zeit'),
        ),
        migrations.AlterField(
            model_name='wednesday',
            name='numbers',
            field=models.CharField(blank=True, verbose_name='Zahl'),
        ),
        migrations.AlterField(
            model_name='wednesday',
            name='time',
            field=models.CharField(blank=True, verbose_name='Zeit'),
        ),
    ]
