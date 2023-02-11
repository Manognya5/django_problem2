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
        abstract = True

class Agent(base_model):
    agent_id = models.IntegerField(primary_key=True)
    agent_name = models.CharField(max_length=100, null=False)
    agent_phone_number = models.CharField(max_length=10, null=False)
    agent_city = models.CharField(max_length=100, null=False)

    def __str__(self):
        return str(self.agent_name)

class Customer(base_model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=100, null=False)
    customer_phone_number = models.CharField(max_length=10, null=False)
    customer_city = models.CharField(max_length=100, null=False)
    agent_id = models.ForeignKey(Agent, related_name='customerAgent', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.customer_name)

class Order(base_model):
    order_id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField(null=False)
    status = (
        ('Pending','Pending'),
        ('In-Transit','In-Transit'),
        ('Delivered','Delivered')
    )
    order_status = models.CharField(max_length=100, choices=status)
    agent_id = models.ForeignKey(Agent, related_name='orderAgent', on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, related_name='orderCustomer', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.order_id)
