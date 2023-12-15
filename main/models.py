from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Receipt(models.Model):
    author= models.ForeignKey(User,on_delete=models.CASCADE,related_name="receipts") 
    store= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    item = models.TextField()
    total_amount = models.FloatField()

    def __str__(self):
        return "{}, {}, {}".format(self.author.username ,self.store ,self.total_amount)