# Generated by Django 4.2.3 on 2023-09-21 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_team_img_team_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('img', models.ImageField(upload_to='team_images')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
