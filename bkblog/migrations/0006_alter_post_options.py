# Generated by Django 4.2.13 on 2024-07-15 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bkblog', '0005_post_featured_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_on']},
        ),
    ]
