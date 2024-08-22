from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    CAT=((1,'Mobile'),(2,'Shoese'),(3,'Cloth'))
    name=models.CharField(max_length=20,verbose_name='Product Name')
    pdetail=models.CharField(max_length=100)
    cat=models.IntegerField(verbose_name='Category',choices=CAT)
    price=models.IntegerField()
    is_active=models.BooleanField(default=True)
    pimage=models.ImageField(upload_to='image')

    def __str__(self):
        return self.name
    
class Cart(models.Model):
   uid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='uid')
   pid=models.ForeignKey('Product',on_delete=models.CASCADE,db_column='pid')
   qty=models.IntegerField(default=1)

class Order(models.Model):
   uid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='uid')
   pid=models.ForeignKey('Product',on_delete=models.CASCADE,db_column='pid')
   qty=models.IntegerField(default=1)
   amt=models.IntegerField()
