# Generated by Django 2.2.16 on 2020-11-18 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_auto_20201118_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='apellido',
            field=models.TextField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='dni',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='post',
            name='nombre',
            field=models.TextField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
