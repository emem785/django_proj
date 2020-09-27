# Generated by Django 3.1.1 on 2020-09-26 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firebase_key', models.CharField(max_length=1000)),
                ('user_name', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]