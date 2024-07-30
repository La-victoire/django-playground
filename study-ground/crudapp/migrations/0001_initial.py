# Generated by Django 5.0.4 on 2024-06-28 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('is_student', models.BooleanField()),
                ('height', models.FloatField()),
                ('registration_date', models.DateTimeField()),
            ],
        ),
    ]
