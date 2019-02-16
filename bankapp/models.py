from django.db import models

# Create your models here.
class BankUser(models.Model):
    username = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

    def __str__(self):
        return str (self.username)

class UserPayMethod(models.Model):
    userid =  models.ForeignKey(BankUser, on_delete = 'do_nothing')
    method =  models.CharField(max_length = 100)

    def __str__(self):
        return str (self.id)

class UserTransaction(models.Model):
     userid =  models.ForeignKey(BankUser, on_delete = 'do_nothing')
     payid  = models.ForeignKey(UserPayMethod, on_delete = 'do_nothing')
     amount = models.IntegerField()