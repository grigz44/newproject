from django.db import models

# Create your models here.


class user(models.Model):
    
    Phone_number = models.CharField(primary_key=True,max_length=10)
    Email = models.EmailField()
    is_customer= models.BooleanField()
    is_admin =models.BooleanField()
    
    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.Phone_number
    
    
class userProfile(models.Model):
    gchoices=((0,'male',),(1,'female'),(2,'others'))
    
    owner = models.OneToOneField(user,on_delete=models.CASCADE)
    Name =models.CharField(max_length=100)
    Date_of_birth = models.DateField()
    Gender = models.IntegerField(choices=gchoices)
    Image = models.ImageField(upload_to='image')
    
    class Meta:
        db_table = 'userprofile'

    def __str__(self):
        return self.Name
    
    
class user_login(models.Model):
    owner = models.ForeignKey(user, blank=True,on_delete=models.CASCADE)
    Otp=    models.IntegerField()
    active =models.BooleanField()
    
    class Meta:
        db_table = 'user_login'


    
   
class product(models.Model):
    Title = models.CharField(max_length=50, blank=True)
    Description=    models.CharField(max_length=500)
    Unique_id =models.AutoField(primary_key=True)
    Price =models.IntegerField()
    
    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.Title
    
    
class product_image(models.Model):
    product = models.ForeignKey(product,blank=True,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productimage')
    
    
    class Meta:
        db_table = 'product_image'

    
    
    
status_choice=((0,'completed'),(1,'pending'))
   
class UserCartProduct(models.Model):
    owner = models.ForeignKey(user, blank=True,on_delete=models.CASCADE)
    product=    models.ForeignKey(product,blank=True,on_delete=models.CASCADE)
    status =models.IntegerField(choices=status_choice)
    
    class Meta:
        db_table = 'UserCartProduct'

    def __str__(self):
        return self.product
    
    
class UserCart(models.Model):
    
    owner = models.OneToOneField(user, blank=True,on_delete=models.CASCADE)
    product=models.ManyToManyField(UserCartProduct,blank=True)
    price = models.IntegerField(blank=True,null=True)
    
    
    class Meta:
        db_table = 'UserCart'

    