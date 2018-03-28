from django.db import models
from django.utils import timezone
from django_mysql.models import JSONField
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    register_date = models.DateTimeField(default=timezone.datetime.now())
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    credit = models.DecimalField(max_digits=20, decimal_places=4)
    gift_credit = models.DecimalField(max_digits=20, decimal_places=4)
    organization_or_person = models.CharField(choices=["organization", "person"])
    

class Peyment(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=4)
    payment_id = models.CharField(max_length=32)
    date = models.DateTimeField(default=timezone.datetime.now())
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Role(models.Model):
    role = models.CharField(choices=["admin", "customer"])
    customers = models.ManyToManyField(Customer)



class Address(models.Model):
    country = models.CharField(max_length=25)
    city = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=30)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Auction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.datetime.now())
    start_date = models.DateField()
    end_date = models.DateField()
    minimum_price_increment = models.DecimalField(max_digits=20, decimal_places=4)

class Item(models.Model):
    price = models.DecimalField(max_digits=20, decimal_places=4)
    off = models.DecimalField(max_digits=20, decimal_places=4)
    made_in = models.CharField(max_length=25)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)

class Store(models.Model):
    name = models.CharField(max_length=25)
    desciption = models.CharField(max_length=255)
    items = models.ManyToManyField(Item)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    Category = models.ForeignKey('Category' , on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=30)
    total_available = models.IntegerField()
    review = models.TextField()
    stars = models.IntegerField()
    details =  JSONField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=2048)
    stars = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Manufacture(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    details =  JSONField()
    products = models.ManyToManyField(Product)

class Order(models.Model):
    create_date = models.DateTimeField(default=timezone.datetime.now())
    modify_date = models.DateTimeField(default=timezone.datetime.now())
    custormer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Offer(models.Model):
    offer_price = models.DecimalField(max_digits=20, decimal_places=4)
    date = models.DateField(default=timezone.datetime.now())
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=4)
    total_bids = models.IntegerField()
    customers = models.ManyToManyField(Customer)


class Shipment(models.Model):
    transport_company = models.CharField(max_length=100)    
    transport_method = models.CharField(max_length=100)  
    send_date = models.DateTimeField()
    recieve_date = models.DateTimeField()
    price = models.DecimalField(max_digits=20, decimal_places=4)
    transport_vehicle = models.CharField(max_length = 50)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Insurance(models.Model):
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=4)
    items = models.ManyToManyField(Item)





