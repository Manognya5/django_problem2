from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        User,
        related_name="%(class)s_createdby",
        on_delete = models.CASCADE,
        null=True
    )

    updated_by = models.ForeignKey(
        User,
        related_name="%(class)s_updatedby",
        on_delete = models.CASCADE,
        null=True
    )
    class Meta:
        abstract = True


class student(BaseModel):
    student_id = models.CharField(max_length=100 , primary_key=True)
    student_first_name = models.CharField(max_length=50 , null = False)
    student_last_name = models.CharField(max_length=50 , null=False)
    student_address = models.CharField(max_length=100 , null=False)
    student_city = models.CharField(max_length=50 , null=False)
    student_state = models.CharField(max_length=50 , null=False)
    student_country = models.CharField(max_length=50 , null=False)


    def __str__(self):
        return str(self.student_first_name)


class lecturer(BaseModel):
    lecturers_id = models.CharField(max_length=100 , primary_key=True)
    lecturer_first_name = models.CharField(max_length= 50 , null=False)
    lecturer_last_name = models.CharField(max_length=50 , null=False)
    
class class_room(BaseModel):
    students_id = models.ForeignKey(
        student , related_name="hello" , on_delete=models.CASCADE
    )
    lecturers_unique_id = models.ForeignKey(
        lecturer , related_name="hiii" , on_delete=models.CASCADE
    )

