# Generated by Django 4.2.13 on 2024-07-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_alter_resources_options_remove_resources_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]