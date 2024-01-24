# Generated by Django 4.2.6 on 2024-01-24 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Owner",
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
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to=None),
                ),
                ("user", models.TextField()),
                ("name", models.TextField()),
                ("phone", models.CharField(max_length=13)),
                ("pets", models.TextField()),
                ("date_created", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Type",
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
                ("name", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Pet",
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
                ("picture", models.ImageField(null=True, upload_to=None)),
                ("owner", models.TextField()),
                ("name", models.TextField()),
                ("age", models.IntegerField()),
                ("gender", models.TextField(null=True)),
                ("description", models.TextField()),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.type"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Adoption",
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
                ("status", models.TextField()),
                ("note", models.TextField(null=True)),
                ("date_created", models.DateTimeField()),
                (
                    "owner",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="app.owner"
                    ),
                ),
                (
                    "pet",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="app.pet"
                    ),
                ),
            ],
        ),
    ]
