# Generated by Django 3.0.1 on 2020-01-03 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20200103_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.DeleteModel(
            name='Author2Book',
        ),
    ]