# Generated by Django 3.0.7 on 2022-03-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(blank=True)),
                ('currency_name', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
