from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class base_model(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(
        User,
        related_name="%(class)s_createdby",
        on_delete=models.CASCADE,
        null=True,
    )
    updated_by = models.ForeignKey(
        User,
        related_name="%(class)s_updatedby",
        on_delete=models.CASCADE,
        null=True,
    ) 
    class Meta:
        abstract=True
#meta

class Retailer(base_model):
    person_id=models.IntegerField(primary_key=True)
    person_name=models.CharField(max_length=100,null=False)
    state=models.CharField(max_length=50,null=False)
    address = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=False)
    zipcode = models.IntegerField(null=True)

    def __str__(self):
        return self.person_name

class Order(base_model):
    order_id = models.IntegerField(primary_key=True)
    purchase_id = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False)
    order_status = (
        ('Pending','Pending'),
        ('In-Transit','In-Transit'),
        ('Delivered','Delivered')
    )
    order_status = models.CharField(max_length=100, choices=order_status)

    def __str__(self):
        return str(self.order_id)

class Denim(base_model):
    serial_id=models.IntegerField(primary_key=True)
    model=models.CharField(max_length=100, null=False)
    status=models.BooleanField()
    person_id = models.ForeignKey(Retailer, related_name='denimperperson', on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, related_name='denimorder', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.serial_id)