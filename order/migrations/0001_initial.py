# Generated by Django 4.2.2 on 2023-09-12 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Clients",
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
                ("company_name", models.TextField()),
                ("contact", models.TextField()),
                ("phone", models.TextField()),
                ("person_in_charge", models.TextField()),
                ("address", models.TextField()),
                ("capital", models.IntegerField()),
                ("listed", models.BooleanField()),
            ],
            options={
                "db_table": "clients",
            },
        ),
        migrations.CreateModel(
            name="Pcs",
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
                ("name", models.TimeField()),
                ("price", models.IntegerField()),
            ],
            options={
                "db_table": "pcs",
            },
        ),
        migrations.CreateModel(
            name="SalesPeople",
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
                ("grade", models.TextField()),
            ],
            options={
                "db_table": "salepeople",
            },
        ),
        migrations.CreateModel(
            name="Orders",
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
                ("date", models.DateField()),
                ("deliver_address", models.TextField()),
                ("contact", models.TextField()),
                ("order_type", models.TextField()),
                ("oder_amount", models.IntegerField()),
                ("pcs_amount", models.IntegerField()),
                ("batery_module_amount", models.IntegerField()),
                ("notice", models.TextField()),
                ("note", models.TextField()),
                (
                    "client_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="order.clients"
                    ),
                ),
                (
                    "pcs_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="order.pcs"
                    ),
                ),
                (
                    "saleperson_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="order.salespeople",
                    ),
                ),
            ],
            options={
                "db_table": "orders",
            },
        ),
    ]
