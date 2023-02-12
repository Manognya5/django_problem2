from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.

# class BaseModel(models.Model):
#     # class Meta:
#     #     abstract = True
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     created_by  = models.ForeignKey(
#         User,
#         related_name="%(class)s_createdby",
#         on_delete=models.CASCADE,
#         null = False
#     )

#     updated_by = models.ForeignKey(
#         User , 
#         related_name="%(class)s_updatedby",
#         on_delete=models.CASCADE,
#         null=False
#     )

class author(models.Model):
    auth_id = models.IntegerField(primary_key=True )
    auth_name = models.CharField(max_length=200 , null=False ,default='')
    place = models.CharField(max_length=200 , null=False ,default='')
    nationality = models.CharField(max_length=200 , null=False ,default='' )
    yob = models.IntegerField(null=False ,default=0)


class book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200 , null = False,default='')
    yop = models.CharField(max_length=200 , null = False ,default='')
    publisher = models.CharField(max_length=200 , null = False,default='')
    author_id = models.ForeignKey(
        author , related_name="author_id" , on_delete=models.CASCADE
    )

