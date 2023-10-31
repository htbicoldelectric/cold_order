from django.db import models
import binascii, os

# Create your models here.


class ManagerLoginToken(models.Model):
    token = models.CharField(max_length=40, primary_key=True)
    time_stamp = models.TimeField(auto_now=True)
    user = models.CharField(max_length=64)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    class Meta:
        managed = True
        db_table = "manage_logging"
