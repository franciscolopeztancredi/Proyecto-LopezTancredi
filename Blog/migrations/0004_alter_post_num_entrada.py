# Generated by Django 4.1.1 on 2022-09-22 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_post_num_entrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='num_entrada',
            field=models.IntegerField(),
        ),
    ]
