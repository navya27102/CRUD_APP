# Generated by Django 5.0.7 on 2024-07-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('position', models.CharField(max_length=25)),
            ],
        ),
    ]
