# Generated by Django 4.1.6 on 2023-07-27 04:38

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_direction_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direction',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]