from django.db import models
from datetime import datetime
import uuid


class Clients(models.Model):
    client_id = models.TextField(primary_key=True, unique=True, editable=False)
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
        
    def save(self, *args, **kwargs):
        if not self.case_id:
            t = datetime.today()
            self.case_id = "COLD-C" + str(uuid.uuid4())
        while Clients.objects.filter(serial_number=self.case_id).exists():
            self.case_id = "COLD-C" + str(uuid.uuid4())
        super(Clients, self).save(*args, **kwargs)


class SalesPeople(models.Model):
    salesperson_id = models.TextField(primary_key=True, unique=True, editable=False)
    name = models.TextField()
    grade = models.TextField()

    class Meta:
        managed = True
        db_table = "salepeople"

    def save(self, *args, **kwargs):
        if not self.case_id:
            t = datetime.today()
            self.case_id = "COLD-S" + str(uuid.uuid4())
        while SalesPeople.objects.filter(serial_number=self.case_id).exists():
            self.case_id = "COLD-S" + str(uuid.uuid4())
        super(SalesPeople, self).save(*args, **kwargs)


class Pcs(models.Model):
    pcs_id = models.TextField(primary_key=True, unique=True, editable=False)
    name = models.TextField()
    price = models.IntegerField()

    class Meta:
        managed = True
        db_table = "pcs"

    def save(self, *args, **kwargs):
        if not self.case_id:
            t = datetime.today()
            self.case_id = "COLD-P" + str(uuid.uuid4())
        while Pcs.objects.filter(serial_number=self.case_id).exists():
            self.case_id = "COLD-P" + str(uuid.uuid4())
        super(Pcs, self).save(*args, **kwargs)


class Products(models.Model):
    product_id = models.TextField(primary_key=True, unique=True, editable=False)
    name = models.TextField()
    price = models.IntegerField()

    class Meta:
        managed = True
        db_table = "products"

    def save(self, *args, **kwargs):
        if not self.case_id:
            t = datetime.today()
            self.case_id = "COLD_I" + str(uuid.uuid4())
        while Products.objects.filter(serial_number=self.case_id).exists():
            self.case_id = "COLD_I" + str(uuid.uuid4())
        super(Products, self).save(*args, **kwargs)


class Cases(models.Model):
    case_id = models.TextField(primary_key=True, unique=True, editable=False)
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
    notice = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "cases"

    def save(self, *args, **kwargs):
        if not self.case_id:
            t = datetime.today()
            self.case_id = f"case{t.year}{t.month}{t.day}" + str(uuid.uuid4())[:4]
        while Cases.objects.filter(serial_number=self.case_id).exists():
            self.case_id = f"case{t.year}{t.month}{t.day}" + str(uuid.uuid4())[:4]
        super(Cases, self).save(*args, **kwargs)


class Orders(models.Model):
    order_id = models.TextField(primary_key=True, unique=True, editable=False)
    client = models.ForeignKey(Clients, models.PROTECT)
    order_apartment = models.TextField()
    order_date = models.DateField()
    delivery_date = models.DateField()
    salesperson = models.ForeignKey(SalesPeople, models.PROTECT)
    deliver_address = models.TextField()
    case = models.ForeignKey(Cases, models.PROTECT)
    contact = models.TextField()
    total_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = "orders"

    def save(self, *args, **kwargs):
        if not self.case_id:
            t = datetime.today()
            self.case_id = f"order{t.year}{t.month}{t.day}" + str(uuid.uuid4())[:4]
        while Orders.objects.filter(serial_number=self.case_id).exists():
            self.case_id = f"order{t.year}{t.month}{t.day}" + str(uuid.uuid4())[:4]
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


class PcsProductOrders(models.Model):
    pcs_product_order_id = models.AutoField(primary_key=True)
    pcs = models.ForeignKey(Pcs, models.PROTECT)
    amount = models.IntegerField()
    product_order = models.ForeignKey(CaseCart, models.PROTECT)

    class Meta:
        managed = True
        db_table = "pcs_product_orders"
