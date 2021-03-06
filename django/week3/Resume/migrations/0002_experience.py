# Generated by Django 2.0.2 on 2018-02-20 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField(blank=True, max_length=64)),
            ],
        ),
    ]
