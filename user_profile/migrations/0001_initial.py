# Generated by Django 3.0.7 on 2022-05-07 11:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('dob', models.DateField(null=True, verbose_name='Date of birth')),
                ('NatID', models.CharField(max_length=200, null=True, verbose_name='National ID')),
                ('address', models.CharField(blank=True, max_length=500)),
                ('medicalAid', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=500, verbose_name='Medical aid')),
                ('medAidName', models.CharField(blank=True, default='None', max_length=200)),
                ('membership', models.CharField(blank=True, default='None', max_length=500)),
                ('beneficiary', models.CharField(blank=True, default='None', max_length=500)),
                ('next_of_kin_name', models.CharField(blank=True, default='None', max_length=500)),
                ('next_of_kin_number', models.CharField(blank=True, default='None', max_length=500)),
                ('status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=8, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
