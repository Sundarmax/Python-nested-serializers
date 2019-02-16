from django.contrib import admin
from .models import BankUser,UserPayMethod,UserTransaction
# Register your models here.
admin.site.register(BankUser)
admin.site.register(UserPayMethod)
admin.site.register(UserTransaction)
