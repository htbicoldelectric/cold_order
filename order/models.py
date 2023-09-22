from django.db import models
from datetime import datetime
import uuid
import hashlib


class Clients(models.Model):
    client_id = models.CharField(
        primary_key=True, unique=True, editable=False, max_length=64
    )
    company_name = models.CharField(max_length=64)
    contact = models.CharField(max_length=64)
    phone = models.CharField(null=False, default="", max_length=64)
    person_in_charge = models.CharField(null=False, default="", max_length=64)
    address = models.CharField(null=False, default="", max_length=64)
    capital = models.IntegerField(null=False, default=0)
    listed = models.BooleanField(null=False, default=False)

    class Meta:
        managed = True
        db_table = "clients"
        app_label = "order"

    def save(self, *args, **kwargs):
        if not self.client_id:
            t = datetime.today()
            self.client_id = "COLD-C" + str(uuid.uuid4())
        while Clients.objects.filter(client_id=self.client_id).exists():
            self.client_id = "COLD-C" + str(uuid.uuid4())
        super(Clients, self).save(*args, **kwargs)


class SalesPeople(models.Model):
    salesperson_id = models.CharField(
        primary_key=True, unique=True, editable=False, max_length=64
    )
    account = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    grade = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = "salepeople"
        app_label = "order"

    def save(self, *args, **kwargs):
        if not self.salesperson_id:
            t = datetime.today()
            self.salesperson_id = "COLD-S" + str(uuid.uuid4())
        while SalesPeople.objects.filter(salesperson_id=self.salesperson_id).exists():
            self.salesperson_id = "COLD-S" + str(uuid.uuid4())
        super(SalesPeople, self).save(*args, **kwargs)


class Pcs(models.Model):
    pcs_id = models.CharField(
        primary_key=True, unique=True, editable=False, max_length=64
    )
    name = models.CharField(max_length=64)
    price = models.IntegerField()

    class Meta:
        managed = True
        db_table = "pcs"
        app_label = "order"

    def save(self, *args, **kwargs):
        if not self.pcs_id:
            t = datetime.today()
            self.pcs_id = "COLD-P" + str(uuid.uuid4())
        while Pcs.objects.filter(pcs_id=self.pcs_id).exists():
            self.pcs_id = "COLD-P" + str(uuid.uuid4())
        super(Pcs, self).save(*args, **kwargs)


class Products(models.Model):
    product_id = models.CharField(
        primary_key=True, unique=True, editable=False, max_length=64
    )
    name = models.CharField(max_length=64)
    price = models.IntegerField()

    class Meta:
        managed = True
        db_table = "products"
        app_label = "order"

    def save(self, *args, **kwargs):
        if not self.product_id:
            t = datetime.today()
            self.product_id = "COLD_I" + str(uuid.uuid4())
        while Products.objects.filter(product_id=self.product_id).exists():
            self.product_id = "COLD_I" + str(uuid.uuid4())
        super(Products, self).save(*args, **kwargs)


class Cases(models.Model):
    case_id = models.CharField(
        primary_key=True, unique=True, editable=False, max_length=64
    )
    address = models.CharField(max_length=64)
    construction_start = models.DateField()
    construction_pre_end = models.DateField()
    construction_end = models.DateField(null=True)
    name = models.CharField(max_length=64)
    construction_team = models.CharField(max_length=64)
    electrical_engineer = models.CharField(max_length=64)
    firefighting_engineer = models.CharField(max_length=64)
    contact = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    vpc_engineer = models.CharField(max_length=64)
    notice = models.CharField(blank=True, null=True, max_length=64)
    note = models.CharField(blank=True, null=True, max_length=64)

    class Meta:
        managed = True
        db_table = "cases"
        app_label = "order"

    def save(self, *args, **kwargs):
        if not self.case_id:
            t = datetime.today()
            self.case_id = f"case{t.year}{t.month}{t.day}" + str(uuid.uuid4())[:4]
        while Cases.objects.filter(case_id=self.case_id).exists():
            self.case_id = f"case{t.year}{t.month}{t.day}" + str(uuid.uuid4())[:4]
        super(Cases, self).save(*args, **kwargs)


class Orders(models.Model):
    order_id = models.CharField(
        primary_key=True, unique=True, editable=False, max_length=64
    )
    client = models.ForeignKey(Clients, models.PROTECT)
    order_apartment = models.CharField(max_length=64)
    order_date = models.DateField()
    delivery_date = models.DateField()
    salesperson = models.ForeignKey(SalesPeople, models.PROTECT)
    deliver_address = models.CharField(max_length=64)
    case = models.ForeignKey(Cases, models.PROTECT)
    contact = models.CharField(max_length=64)
    total_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = "orders"
        app_label = "order"

    def save(self, *args, **kwargs):
        if not self.order_id:
            t = datetime.today()
            self.order_id = f"order{t.year}{t.month}{t.day}" + str(uuid.uuid4())[:4]
        while Orders.objects.filter(order_id=self.order_id).exists():
            self.order_id = f"order{t.year}{t.month}{t.day}" + str(uuid.uuid4())[:4]
        super(Orders, self).save(*args, **kwargs)


class CaseCart(models.Model):
    case_cart_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Products, models.PROTECT)
    amount = models.IntegerField()
    total_price = models.IntegerField()
    order = models.ForeignKey(Orders, models.PROTECT)

    class Meta:
        managed = True
        db_table = "case_cart"
        app_label = "order"


class PcsProductOrders(models.Model):
    pcs_product_order_id = models.AutoField(primary_key=True)
    pcs = models.ForeignKey(Pcs, models.PROTECT)
    amount = models.IntegerField()
    product_order = models.ForeignKey(CaseCart, models.PROTECT)

    class Meta:
        managed = True
        db_table = "pcs_product_orders"
        app_label = "order"
