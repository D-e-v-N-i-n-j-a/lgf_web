# Generated by Django 4.2.3 on 2023-09-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnershipForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('firstname', models.CharField(max_length=255, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=255, verbose_name='Last Name')),
                ('organizations', models.CharField(max_length=255, verbose_name='Organizations')),
                ('contact_number', models.CharField(max_length=20, verbose_name='Contact Number')),
                ('country', models.CharField(max_length=255, verbose_name='Country')),
                ('area_of_interest', models.CharField(max_length=255, verbose_name='Area of Interest')),
                ('summary_of_proposed_partnership', models.TextField(max_length=800, verbose_name='Summary of Proposed Partnership')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('finish_date', models.DateField(verbose_name='Finish Date')),
                ('partnership_duration', models.CharField(max_length=255, verbose_name='Partnership Duration')),
                ('sponsorship_amount', models.CharField(max_length=255, verbose_name='Sponsorship Amount')),
            ],
        ),
    ]
