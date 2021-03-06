# Generated by Django 3.0.1 on 2020-01-03 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app01', '0006_auto_20200103_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=32)),
                ('tel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('pub_date', models.DateTimeField()),
                ('authors', models.ManyToManyField(to='app01.Author')),
                ('publish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publish')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='ad',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.AuthorDetail'),
        ),
    ]
