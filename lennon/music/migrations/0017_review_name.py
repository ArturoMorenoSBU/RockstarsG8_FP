# Generated by Django 2.2.5 on 2022-05-11 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0016_song_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
