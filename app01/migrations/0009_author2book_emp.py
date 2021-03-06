# Generated by Django 3.0.1 on 2020-02-15 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_auto_20200105_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('dep', models.CharField(max_length=32)),
                ('pro', models.CharField(max_length=32)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Author2Book',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Book')),
            ],
        ),
    ]
