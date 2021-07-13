from django.db import models
from djrichtextfield.models import RichTextField

class Carcategory(models.Model):
    name = models.CharField(max_length=30,null=True)
    image = models.FileField(null=True)
    def __str__(self):
        return self.name

class cars(models.Model):
    category = models.ForeignKey(Carcategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30,null=True)
    model = models.IntegerField( null=True)
    image = models.FileField(null=True)
    price = models.IntegerField(null=True)
    discription = models.TextField(null=True)

class Contact(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.EmailField( null=True)
    subject = models.CharField(max_length=30,null=True)
    message = models.TextField(null=True)

class TERMS_CONDITIONSs(models.Model):
    cont = RichTextField(null=True)

class PRIVACY_POLICYs(models.Model):
    cont = RichTextField(null=True)

class PAYMENT_PROCEDUREs(models.Model):
    cont = RichTextField(null=True)

class BOOKING_TIPS(models.Model):
    cont = RichTextField(null=True)

class FAQQS(models.Model):
    cont = RichTextField(null=True)

