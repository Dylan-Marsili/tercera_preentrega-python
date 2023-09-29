# Generated by Django 4.2.5 on 2023-09-29 00:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AppClinica", "0003_delete_profesor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Empleado",
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
                ("nombre", models.CharField(max_length=40)),
                ("apellido", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=40)),
                ("cargo", models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name="Curso",
        ),
    ]
