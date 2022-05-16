# Generated by Django 4.0.4 on 2022-05-16 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=60)),
                ('CourseNumber', models.IntegerField(max_length=10)),
                ('InstructorName', models.CharField(default='', max_length=80)),
                ('Duration', models.FloatField(max_length=20)),
            ],
        ),
    ]
