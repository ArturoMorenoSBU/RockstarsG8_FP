# Generated by Django 3.0.8 on 2022-05-05 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20220504_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='file',
            field=models.FileField(default='Some String', upload_to='static/songs/'),
        ),
    ]
