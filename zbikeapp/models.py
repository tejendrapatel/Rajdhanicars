from django.core.mail import message
from django.db import models
from djrichtextfield.models import RichTextField

class happy_clients(models.Model):
    image = models.FileField(null=True)

class fcli(models.Model):
    image = models.FileField(null=True)

class Carcategory(models.Model):
    name = models.CharField(max_length=30,null=True)
    image = models.FileField(null=True)
    def __str__(self):
        return self.name


class Verifications(models.Model):
    name = models.CharField(max_length=30,null=True)
    mobile = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    temporary = models.IntegerField(null=True)
    date= models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class testdrive(models.Model):
    name = models.CharField(max_length=30,null=True)
    mobile = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)
    date= models.DateField(auto_now=True)
    time= models.TimeField(auto_now=True)
    def __str__(self):
        return self.name
    


class Newsletter(models.Model):
    email = models.EmailField(null=True)
    def __str__(self):
        return self.email

class MAIN_BANNER(models.Model):
    aimage = models.FileField(null=True)
    bimage = models.FileField(null=True)
    cimage = models.FileField(null=True)
   

class cars(models.Model):
    OWNER_CHOICES = [("1", "1"),("2", "2"),("3", "3"),("more_than_4", "more_than_4")]
    FUEL_CHOICES = [("petrol", "petrol"),("diesel", "diesel"),("other", "other")]
    MODEL_CHOICES = [("2001", "2001"),("2002", "2002"),("2003", "2003"),("2004", "2004"),("2005", "2005"),("2006", "2006"),("2007", "2007"),("2008", "2008"),("2009", "2009"),("2010", "2010"),("2011", "2011"),("2012", "2012"),("2013", "2013"),("2014", "2014"),("2015", "2015"),("2016", "2016"),("2017", "2017"),("2018", "2018"),("2019", "2019"),("2020", "2020"),("2021", "2021"),("2022","2022"),("Latest","Latest")]
    INSURANCE_CHOICES = [("comprehensive", "comprehensive"),("third_party", "third_party"),("expired", "expired")]
    REGISTRATION_CHOICES = [("unregistred", "unregistred"),("Individual", "Individual"),("Corporate", "Corporate"),("Taxi", "Taxi"),("commercial_registration", "commercial_registration")]
    category = models.ForeignKey(Carcategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30,null=True)
    varient = models.CharField(max_length=30,null=True)
    model = models.CharField(max_length=30, choices=MODEL_CHOICES, default='Latest')
    fuel_type = models.CharField(max_length=30, choices=FUEL_CHOICES, default='petrol')
    kilometer = models.IntegerField(null=True)
    colour = models.CharField(null=True,max_length=20)
    registration_type = models.CharField(max_length=30, choices=REGISTRATION_CHOICES, default='Individual')
    registration_No = models.CharField(null=True,max_length=10) 
    Insurance = models.CharField(max_length=30, choices=INSURANCE_CHOICES, default='comprehensive')  
    owners = models.CharField(max_length=30, choices=OWNER_CHOICES, default='1')
    price = models.IntegerField(null=True)
    discription = models.TextField(null=True)
    image = models.FileField(null=True,blank=True)
    image2 = models.FileField(null=True)
    image3 = models.FileField(null=True)
    image4 = models.FileField(null=True)
    image5 = models.FileField(null=True)
    image6 = models.FileField(null=True)
    image7 = models.FileField(null=True)
    image8 = models.FileField(null=True)
    image9 = models.FileField(null=True)
   
    def __str__(self):
        return self.name

    

class Contact(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.EmailField( null=True)
    subject = models.IntegerField(null=True)
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

