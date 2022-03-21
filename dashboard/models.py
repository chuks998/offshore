# from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import string, random

# Create your models here.
def account_genarator(length=11, var=string.digits):
    return ''.join(random.choice(var) for _ in range(length))


class AccountDetail(models.Model):
    account_holder = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(default=account_genarator, max_length=11, unique=True, blank=True, null=True)
    account_balance = models.FloatField(default=0.00)
    
    class META:
        verbose_name_plural = 'AccountDetails'

    def __str__(self):
        return f'{self.account_holder}'

    def save(self):
            super().save()


class Transfer(models.Model):
    sending_user = models.ForeignKey(User, on_delete=models.CASCADE)
    reciver_name = models.CharField(max_length=100)
    reciver_account = models.CharField(max_length=12)
    amount = models.FloatField(default=0.00)
    desc = models.CharField(max_length=200, default='Nil')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.sending_user}'

    # def save(self):
    #     self.sending_user.account_balance -= self.amount
    #     self.save()
