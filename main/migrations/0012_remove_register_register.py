# Generated by Django 4.1.6 on 2023-07-25 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_userresult_uqa_user_result_uqa_answer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='register',
        ),
    ]
