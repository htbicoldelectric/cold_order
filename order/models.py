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
        managed = True
        db_table = "clients"


class SalesPeople(models.Model):
    salesperson_id = models.TextField(unique=True)
    name = models.TextField()
    grade = models.TextField()

    class Meta:
        managed = True
        db_table = "salepeople"


class Pcs(models.Model):
    pcs_id = models.TextField(unique=True)
    name = models.TextField()
    price = models.IntegerField()

    class Meta:
        managed = True
        db_table = "pcs"


class Products(models.Model):
    product_id = models.TextField(unique=True)
    name = models.TextField()
    price = models.IntegerField()

    class Meta:
        managed = True
        db_table = "products"


class Cases(models.Model):
    case_id = models.TextField(unique=True)
    address = models.TextField()
    construction_start = models.DateField()
    construction_pre_end = models.DateField()
    construction_end = models.DateField(null=True)
    name = models.TextField()
    construction_team = models.TextField()
    electrical_engineer = models.TextField()
    firefighting_engineer = models.TextField()
    contact = models.TextField()
    phone = models.TextField()
    vpc_engineer = models.TextField()

    class Meta:
        managed = True
        db_table = "cases"


class Orders(models.Model):
    order_id = models.TextField(unique=True)
    date = models.DateField()
    client = models.ForeignKey(Clients, models.PROTECT)
    salesperson = models.ForeignKey(SalesPeople, models.PROTECT)
    deliver_address = models.TextField()
    case = models.ForeignKey(Cases, models.PROTECT)
    contact = models.TextField()
    order_type = models.TextField()
    oder_amount = models.IntegerField()
    pcs_id = models.ForeignKey(Pcs, models.PROTECT)
    pcs_amount = models.IntegerField()
    batery_module_amount = models.IntegerField()
    notice = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    cancel = models.BooleanField()

    class Meta:
        managed = True
        db_table = "orders"


class ProductOrders(models.Model):
    product_order_id = models.TextField(unique=True)
    product = models.ForeignKey(Products, models.PROTECT)
    amount = models.IntegerField()
    total_price = models.IntegerField()
    order = models.ForeignKey(Orders, models.PROTECT)
    cancel = models.BooleanField()

    class Meta:
        managed = True
        db_table = "product_orders"

class PcsProductOrders(models.Model):
    pcs_product_order_id = models.TextField(unique=True)
    pcs = models.ForeignKey(Pcs, models.PROTECT)
    amount = models.IntegerField()
    product_order = models.ForeignKey(ProductOrders, models.PROTECT)

    class Meta:
        managed = True
        db_table = "pcs_product_orders"
