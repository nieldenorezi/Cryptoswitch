from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.

class CryptoAccount(models.Model):
    CRYPTO_CHOICES = (
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crypto_type = models.CharField(max_length=3, choices=CRYPTO_CHOICES)
    balance = models.DecimalField(max_digits=20, decimal_places=8, default=0)
    bonus_balance = models.DecimalField(max_digits=20, decimal_places=8, default=0)
    # referral_balance = models.DecimalField(max_digits=20, decimal_places=8, default=0)
    
    
    

    def __str__(self):
        return str(self.balance)


class Transaction(models.Model):
    TRANSACTION_CHOICES = (
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAWAL', 'Withdrawal'),
    )
    
    crypto_account = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_CHOICES)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    date = models.DateTimeField(auto_now_add=True)
    
   
    def __str__(self):
        return str(self.amount)
    
    
    def save(self, *args, **kwargs):
        if self.transaction_type == 'DEPOSIT':
            self.crypto_account.balance += self.amount
        elif self.transaction_type == 'WITHDRAWAL':
            if self.amount > self.crypto_account.balance:
                raise ValidationError("Insufficient Balance for Withdrawal")
            self.crypto_account.balance -= self.amount
        self.crypto_account.save()
        super().save(*args, **kwargs)
    
    
    








