# Generated by Django 5.1.3 on 2025-03-25 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0004_userprofile_delete_rating"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userprofile",
            options={"verbose_name_plural": "UserProfiles"},
        ),
    ]
