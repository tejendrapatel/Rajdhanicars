from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from zbikeapp.models import *
from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from frontend.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
def HOME(request):
    li = []
    ca = cars.objects.all()

    carr= Carcategory.objects.all()
    d = {"ca":ca,"carr":carr}
    return render(request,'tt.html',d)

def ABOUT(request):
    return render(request,'about.html')

def CONTACT(request):
    if request.method == "POST":
        f = request.POST
        content = f['message']
        nam = f['name']
        ema = f['email']
        subje = f['sub']
        Contact.objects.create(name=nam, email=ema, subject=subje, message=content)
        email = 'tejendrapatel1998@gmail.com'
        subject = subje
        msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{email}'])
        d = {'subject': subject, "content": content}
        html = get_template('email/email.html').render(d)
        msg.attach_alternative(html, 'text/html')
        msg.send()
    return render(request,'contact.html')

def BIKES(request):
    ca = cars.objects.all()
    d = {"ca":ca}
    return render(request,'car.html',d)

def SERVICES(request):
    return render(request,'services.html')


def PRICING(request):
    return render(request, 'pricing.html')

def TERMS_CONDITIONS(request):
    ter = TERMS_CONDITIONSs.objects.all()
    d = {"ter": ter}
    return render(request, 'terms_conditions.html',d)

def PRIVACY_POLICY(request):
    ter = PRIVACY_POLICYs.objects.all()
    d = {"ter": ter}
    return render(request, 'privacy_policy.html',d)

def PAYMENT_PROCEDURE(request):
    ter = PAYMENT_PROCEDUREs.objects.all()
    d = {"ter": ter}
    return render(request, 'payment_procedure.html',d)


def BOOKING_TIPss(request):
    ter = BOOKING_TIPS.objects.all()
    d = {"ter": ter}
    return render(request, 'buying_tips.html',d)

def FAQS(request):
    ter = FAQQS.objects.all()
    d = {"ter": ter}
    return render(request, 'faqs.html',d)

######## DYNAMIC URLS   ########

def CAR_SINGLE(request,car_id):
    carss = cars.objects.get(id=car_id)
    d = {"carss":carss}
    return render(request, 'car_detail.html',d)

def CAR_CATEGORY_FILTER(request,car_id):
    single = Carcategory.objects.get(id=car_id)
    carsingle = cars.objects.filter(category=single)
    d = {"carsingle":carsingle}
    return render(request, 'car_category_filter.html',d)