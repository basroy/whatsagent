# Generated by Django 4.0.6 on 2022-10-03 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_is_active_user_terms_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='name',
        ),
    ]
