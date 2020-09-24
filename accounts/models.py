from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    date_created =models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CategoryItem = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )
    name = models.CharField(max_length=60)
    price = models.FloatField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True, choices=CategoryItem)
    description = models.TextField(max_length=700, null=True)
    date_created =models.DateTimeField(null=True, auto_now_add=True)
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=60, null=True)
    def __str__(self):
        return self.name
    



class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Cancell', 'Cancell'),
        ('Aapproved', 'Approved'),
        ('Ddelivery', 'Delivery'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=100, null=True, choices=STATUS)
    date_created =models.DateTimeField(null=True, auto_now_add=True)
    tag =models.ManyToManyField(Tag)

    def __str__(self):
        return self.status
