# Generated by Django 4.1.6 on 2023-07-27 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_rename_score_to_be_awarded_direction_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresult',
            name='incorrect',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
