# Generated by Django 3.2.18 on 2023-05-09 08:49

from django.db import migrations, models
import saleor.order.models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0166_copy_number_to_number_as_str"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.AlterField(
                    model_name="order",
                    name="number",
                    field=models.IntegerField(blank=True, null=True, unique=True),
                ),
            ],
            state_operations=[
                migrations.RemoveField(
                    model_name="order",
                    name="number",
                ),
            ],
        ),
        migrations.AlterField(
            model_name="order",
            name="number_as_str",
            field=models.CharField(
                default=saleor.order.models.get_order_number,
                editable=False,
                max_length=64,
                unique=True,
            ),
        ),
        migrations.AlterModelOptions(
            name="order",
            options={
                "ordering": ("-updated_at",),
                "permissions": (("manage_orders", "Manage orders."),),
            },
        ),
    ]