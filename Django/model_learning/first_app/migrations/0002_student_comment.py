# Generated by Django 5.0.6 on 2024-05-21 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("first_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="comment",
            field=models.CharField(default="not available", max_length=40),
        ),
    ]
