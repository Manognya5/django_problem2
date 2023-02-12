from django.contrib import admin

# Register your models here.
from .models import author , book
# Register your models here.


admin.site.register(book)
admin.site.register(author)
