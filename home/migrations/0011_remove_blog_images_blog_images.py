# Generated by Django 4.2.3 on 2023-10-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_ourwork'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='images',
        ),
        migrations.AddField(
            model_name='blog',
            name='images',
            field=models.ImageField(default=1, upload_to='blog_image'),
            preserve_default=False,
        ),
    ]
