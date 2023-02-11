from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(
        User,
        related_name="%(class)s_createdby",
        on_delete=models.CASCADE,
        null=True,
    )
    updated_by=models.ForeignKey(
        User,
        related_name="%(class)s_updatedby",
        on_delete=models.CASCADE,
        null=True,
    )


class Details(BaseModel):
    user_id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100,null=False)
    address=models.CharField(max_length=100,null=False)
    state=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=False)
    zipcode=models.IntegerField(null=True)
    #def  __str__(self) -> str:
        #return self.user_id
class Order(BaseModel):
    order_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=100,null=False)
    price=models.IntegerField(null=False)
    payment_status=models.BooleanField(null=False)
    user_id=models.IntegerField()
    user_id=models.ForeignKey(Details,on_delete=models.CASCADE)
    def  __str__(self) -> str:
        return self.order_id

    
