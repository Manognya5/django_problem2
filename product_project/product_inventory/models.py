from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, related_name="%(class)s_createdby", on_delete=models.CASCADE, null=True
    )
    updated_by = models.ForeignKey(
        User, related_name="%(class)s_updatedby", on_delete=models.CASCADE, null=True
    )

    class Meta:
        abstract = True


class Store(BaseModel):
    store_id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=False)
    zipcode = models.IntegerField(null=True)

    def __str__(self):
        return str(self.store_id)


class Product(BaseModel):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100, null=False)
    store_id = models.ForeignKey(
        Store, related_name="prodfromstore", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.product_id)


class Customer(BaseModel):
    cust_id = models.IntegerField(primary_key=True)
    cust_name = models.CharField(max_length=100, null=False)
    product_id = models.ForeignKey(
        Product, related_name="prodbycust", on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False)
    total = models.IntegerField(null=False)

    def __str__(self):
        return str(self.cust_id)
