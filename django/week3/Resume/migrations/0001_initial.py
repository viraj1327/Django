# Generated by Django 2.0.2 on 2018-02-19 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('degree', models.CharField(max_length=64)),
                ('major', models.CharField(max_length=64)),
                ('gpa', models.FloatField()),
            ],
        ),
    ]
