# Generated by Django 4.1.1 on 2022-10-17 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0012_remove_post_tags_delete_tag'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comentario',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]