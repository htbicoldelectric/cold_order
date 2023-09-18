from django.db import models


class Clients(models.Model):
    client_id = models.TextField(unique=True)
    company_name = models.TextField()
    contact = models.TextField()
    phone = models.TextField(null=False, default="")
    person_in_charge = models.TextField(null=False, default="")
    address = models.TextField(null=False, default="")
    capital = models.IntegerField(null=False, default=0)
    listed = models.BooleanField(null=False, default=False)

    class Meta:
        managed = False
        db_table = "clients"


class SalesPeople(models.Model):
    salesperson_id = models.TextField(unique=True)
    name = models.TextField()
    grade = models.TextField()

    class Meta:
        managed = False
        db_table = "salepeople"


class Pcs(models.Model):
    pcs_id = models.TextField(unique=True)
    name = models.TimeField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = "pcs"


class Products(models.Model):
    product_id = models.TextField(unique=True)
    name = models.TextField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = "products"


class Orders(models.Model):
    order_id = models.TextField(unique=True)
    date = models.DateField()
    client_id = models.ForeignKey(Clients, models.PROTECT)
    saleperson_id = models.ForeignKey(SalesPeople, models.PROTECT)
    deliver_address = models.TextField()
    contact = models.TextField()
    order_type = models.TextField()
    oder_amount = models.IntegerField()
    pcs_id = models.ForeignKey(Pcs, models.PROTECT)
    pcs_amount = models.IntegerField(null=False)
    batery_module_amount = models.IntegerField()
    notice = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    cancel = models.BooleanField()

    class Meta:
        managed = False
        db_table = "orders"


class ProductOrders(models.Model):
    product_order_id = models.TextField(unique=True)
    product_id = models.ForeignKey(Products, models.PROTECT)
    amount = models.IntegerField()
    total_price = models.IntegerField()
    order_id = models.ForeignKey(Orders, models.PROTECT)
    cancel = models.BooleanField()

    class Meta:
        managed = False
        db_table = "product_orders"
