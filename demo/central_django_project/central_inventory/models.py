from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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
        abstract = True

class Site(BaseModel):
    site_id = models.IntegerField(primary_key=True)
    site_name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null = False)
    state = models.CharField(max_length=100, null = True)
    country = models.CharField(max_length=100, null = False)
    zipcode = models.IntegerField(null = True)

    def __str__(self):
        return self.site_name

class Order(BaseModel):
    STATUS = (
        #key - value
        ('Pending', 'Pending'),
        ('In-Transit', 'In-Transit'),
        ('Delivered', 'Delivered')
    )
    order_id = models.IntegerField(primary_key=True, null=False)
    purchase_id = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False)
    device_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return str(self.order_id)

class IAP(BaseModel):
    serial_number = models.IntegerField(primary_key=True, null=False)
    ip_aadr = models.CharField(max_length=15, null=False)
    mac_addr = models.CharField(max_length=17, null=False)
    model = models.CharField(max_length=100, null=False)
    is_vc = models.BooleanField()
    site_id = models.ForeignKey(Site, related_name='iappersite', on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, related_name='iaporder', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.serial_number)

class Switch(BaseModel):
    serial_number = models.IntegerField(primary_key=True, null=False)
    ip_aadr = models.CharField(max_length=15, null=False)
    mac_addr = models.CharField(max_length=17, null=False)
    model = models.CharField(max_length=100, null=False)
    site_id = models.ForeignKey(Site, related_name='swpersite', on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, related_name='sworder', on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.serial_number)




