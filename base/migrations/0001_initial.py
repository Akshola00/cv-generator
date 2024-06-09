# Generated by Django 4.2.7 on 2024-06-09 13:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=200)),
                ("phone", models.BigIntegerField(max_length=200)),
                ("summary", models.TextField(max_length=2000)),
                ("degree", models.TextField(max_length=200)),
                ("school", models.TextField(max_length=200)),
                ("university", models.TextField(max_length=200)),
                ("previous_work", models.TextField(max_length=2000)),
                ("skills", models.TextField(max_length=1000)),
            ],
        ),
    ]
