from django.db import models

# Create your models here.


class Clients(models.Model):
    client_id = models.TextField(unique=True, default="")
    company_name = models.TextField()
    contact = models.TextField()
    phone = models.TextField()
    person_in_charge = models.TextField()
    address = models.TextField()
    capital = models.IntegerField()
    listed = models.BooleanField()

    class Meta:
        db_table = "clients"


class SalesPeople(models.Model):
    salesperson_id = models.TextField(unique=True, default="")
    name = models.TextField()
    grade = models.TextField()

    class Meta:
        db_table = "salepeople"


class Pcs(models.Model):
    pcs_id = models.TextField(unique=True, default="")
    name = models.TimeField()
    price = models.IntegerField()

    class Meta:
        db_table = "pcs"


class Orders(models.Model):
    order_id = models.TextField(unique=True, default="")
    date = models.DateField()
    client_id = models.ForeignKey(Clients, on_delete=models.PROTECT)
    saleperson_id = models.ForeignKey(SalesPeople, on_delete=models.PROTECT)
    deliver_address = models.TextField()
    contact = models.TextField()
    order_type = models.TextField()
    oder_amount = models.IntegerField()
    pcs_id = models.ForeignKey(Pcs, on_delete=models.PROTECT)
    pcs_amount = models.IntegerField(null=False)
    batery_module_amount = models.IntegerField()
    notice = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "orders"
