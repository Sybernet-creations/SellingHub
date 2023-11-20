from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image


# Create your models here.
class Product(models.Model):
    
    Product_Id = models.CharField(max_length=255,blank=False,unique=True,primary_key=True)
    Product_Name = models.CharField(max_length=255,blank=False,)
    Product_Category = models.CharField(max_length=255, 
                                        choices=(
                                            ('Education','Education'),('Business','Business'),('Other','Other')
                                        )
                                        )
    Product_Description = models.TextField(blank=False)
    Product_Price = models.FloatField(blank=False,validators=[MinValueValidator(1.0)])
    Product_Image = models.ImageField(upload_to='product_images/')
    total_rating = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    rank = models.FloatField(default=0.0)
    
    def update_rank(self):
        if self.total_rating != 0:
            self.rank = self.rating / self.total_rating
            self.save()
            
class ProductRating(models.Model):
    RATINGS = (
        (1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"),
    )
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    rating = models.IntegerField(choices = RATINGS)
    
    def save(self,*args,**kwargs):
        self.product.total_rating +=1
        self.product.rating += self.rating
        self.product.update_rank()
        super().save(*args,**kwargs)