# Generated by Django 4.1.1 on 2022-09-22 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_alter_post_image_alter_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='fecha',
        ),
    ]
