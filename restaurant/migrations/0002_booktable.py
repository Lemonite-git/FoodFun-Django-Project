# Generated by Django 3.0.5 on 2020-04-20 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]