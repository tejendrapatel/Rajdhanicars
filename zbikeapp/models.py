from django.db import models
from djrichtextfield.models import RichTextField

class cli(models.Model):
    image = models.FileField(null=True)


class Carcategory(models.Model):
    name = models.CharField(max_length=30,null=True)
    image = models.FileField(null=True)
    def __str__(self):
        return self.name
    

class cars(models.Model):
    OWNER_CHOICES = [("1", "1"),("2", "2"),("3", "3"),("more_than_4", "more_than_4")]
    INSURANCE_CHOICES = [("comprehensive", "comprehensive"),("third_party", "third_party"),("expired", "expired")]
    REGISTRATION_CHOICES = [("unregistred", "unregistred"),("Individual", "Individual"),("Corporate", "Corporate"),("Taxi", "Taxi"),("commercial_registration", "commercial_registration")]
    model = models.TextField(null=True)
    category = models.ForeignKey(Carcategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30,null=True)
    model = models.IntegerField( null=True)
    fuel_type = models.CharField(null=True,max_length=10)
    kilometer = models.IntegerField(null=True)
    colour_family = models.CharField(null=True,max_length=20)
    registration_type = models.CharField(max_length=30, choices=REGISTRATION_CHOICES, default='Individual')
    registration_No = models.IntegerField(null=True) 
    Insurance = models.CharField(max_length=30, choices=INSURANCE_CHOICES, default='comprehensive')  
    owners = models.CharField(max_length=30, choices=OWNER_CHOICES, default='1')
    price = models.IntegerField(null=True)
    Video = models.FileField(null=True)
    Date_of_add = models.DateField(auto_now=True)
    image = models.FileField(null=True)
    image2 = models.FileField(null=True)
    image3 = models.FileField(null=True)
    image4 = models.FileField(null=True)
    image5 = models.FileField(null=True)
    image6 = models.FileField(null=True)
    image7 = models.FileField(null=True)
    image8 = models.FileField(null=True)
    image9 = models.FileField(null=True)
   
    

    

class Contact(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.EmailField( null=True)
    subject = models.CharField(max_length=30,null=True)
    message = models.TextField(null=True)

class video(models.Model):
    Video = models.URLField(null=True)

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

