from django.db import models
from django.contrib.auth.models import User 


class BaseModel(models.Model):
    created_by= models.DateTimeField(auto_now_add=True)
    updated_by= models.DateTimeField(auto_now=True)
    created_by= models.ForeignKey(
        User,
        related_name="%(class)s_createdby",
        on_delete=models.CASCADE,
        null=True,
    )
    updated_by= models.ForeignKey(
        User,
        related_name="%(class)s_updatedby",
        on_delete=models.CASCADE,
        null=True,
    )
    
    class Meta:
        abstract = True

# Create your models here.
class Site(BaseModel):
    site_id = models.IntegerField(primary_key=True)
    site_name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=False)
    zipcode = models.IntegerField(null=True)

    def __str__(self):
        return str(self.site_name)

class Order(BaseModel):
    STATUS = (
        ('Pending', 'Pending'),
        ('In-Transit', 'In-Transit'),
        ('Delivered', 'Delivered')
    )
    order_id = models.IntegerField(primary_key=True)
    purchase_id = models.IntegerField(null=False)
    quantity = models.IntegerField()
    type = models.CharField(max_length=100, null=True)
    csm_name = models.CharField(max_length=100, null=False)
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return str(self.order_id
)

class IAP(BaseModel):
    serial = models.CharField(max_length=100,primary_key=True)
    ip_address = models.CharField(max_length=100, null=False)
    mac_address = models.CharField(max_length=100, null=False)
    model = models.CharField(max_length=100, null=False)
    status = models.CharField(max_length=100, null=True)
    is_vc = models.BooleanField(default=False)
    site_id = models.ForeignKey(Site, related_name='iappersite', on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, related_name='iaporder', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.serial)

class Switch(BaseModel):
    serial = models.CharField(max_length=100,primary_key=True)
    ip_address = models.CharField(max_length=100, null=False)
    mac_address = models.CharField(max_length=100, null=False)
    model = models.CharField(max_length=100, null=False)
    status = models.BooleanField(null=False)
    site_id = models.ForeignKey(Site, related_name='swpersite', on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, related_name='sworder', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.serial)

