# Generated by Django 4.1.7 on 2023-02-28 03:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shows", "0027_move_sub_shows_to_parent_show"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="show",
            name="sub_shows",
        ),
    ]
