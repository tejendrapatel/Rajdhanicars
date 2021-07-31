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
import random
from frontend.settings import account_sid,auth_token,my_twilio


def VERIFICATION(request):
    if request.method == "POST":
        f = request.POST
        namee = f['nam']
        emaii = f['ema']
        mobb = f['mob']
        ra=random.randint(1000,9999)
        temp=ra
        subject = "Congratulation "
        content = ' "you are succesfully registered in Authenticator your security code is "{}" '.format(temp)
        msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{emaii}'])
        msg.send()
        if Verifications.objects.filter(mobile=mobb).exists():
            Verifications.objects.update(name=namee, email=emaii, mobile=mobb, temporary = temp)
            return redirect('verification_otp')
        else:
            Verifications.objects.create(name=namee, email=emaii, mobile=mobb, temporary = temp)
            return redirect('verification_otp')
        
    you =  video.objects.all()
    you2 = you[:2]
    ca = cars.objects.all()
    price50 = [p for p in cars.objects.all() if (p.price >= 50000 and p.price <=100000)]
    price100 = [p for p in cars.objects.all() if (p.price >= 100000 and p.price <=200000)]
    price200 = [p for p in cars.objects.all() if (p.price >= 200000 and p.price <=300000)]
    price500 = [p for p in cars.objects.all() if (p.price >= 300000 and p.price <=500000)]
    carr= Carcategory.objects.all()
    clientss = cli.objects.all()
    fclientss = fcli.objects.all()
    d = {"ca":ca,"carr":carr,"price50":price50,"price100":price100,"price200":price200,"price500":price500,"fclientss":fclientss,"clientss":clientss,"you":you,"you2":you2}
    return render(request,'verification.html')

def VERIFICATION_OTP(request):
    if request.method == "POST":
        f = request.POST
        namees = f['zzz']
        if Verifications.objects.filter(temporary=namees).exists():
            return redirect('home')
        else:
            return redirect('verification')
    you =  video.objects.all()
    you2 = you[:2]
    ca = cars.objects.all()
    price50 = [p for p in cars.objects.all() if (p.price >= 50000 and p.price <=100000)]
    price100 = [p for p in cars.objects.all() if (p.price >= 100000 and p.price <=200000)]
    price200 = [p for p in cars.objects.all() if (p.price >= 200000 and p.price <=300000)]
    price500 = [p for p in cars.objects.all() if (p.price >= 300000 and p.price <=500000)]
    carr= Carcategory.objects.all()
    clientss = cli.objects.all()
    fclientss = fcli.objects.all()
    d = {"ca":ca,"carr":carr,"price50":price50,"price100":price100,"price200":price200,"price500":price500,"fclientss":fclientss,"clientss":clientss,"you":you,"you2":you2}
    return render(request,'verification_otp.html')

def HOME(request):
    if request.method == "POST":
        f = request.POST
        emm = f['ema']
        Newsletter.objects.create(email=emm)
    you =  video.objects.all()
    you2 = you[:2]
    ca = cars.objects.all()
    price50 = [p for p in cars.objects.all() if (p.price >= 50000 and p.price <=100000)]
    price100 = [p for p in cars.objects.all() if (p.price >= 100000 and p.price <=200000)]
    price200 = [p for p in cars.objects.all() if (p.price >= 200000 and p.price <=300000)]
    price500 = [p for p in cars.objects.all() if (p.price >= 300000 and p.price <=500000)]
    carr= Carcategory.objects.all()
    clientss = cli.objects.all()
    fclientss = fcli.objects.all()
    d = {"ca":ca,"carr":carr,"price50":price50,"price100":price100,"price200":price200,"price500":price500,"fclientss":fclientss,"clientss":clientss,"you":you,"you2":you2}
    return render(request,'index.html',d)

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
    fclientss = fcli.objects.all()
    d = {"fclientss":fclientss}
    return render(request,'services.html',d)


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

def CAR_PRICE1(request):
    price50 = [p for p in cars.objects.all() if (p.price >= 50000 and p.price <=100000)]
    d = {"price50":price50}
    return render(request,'carprice_filter1.html',d)
def CAR_PRICE2(request):
    price100 = [p for p in cars.objects.all() if (p.price >= 100000 and p.price <=200000)]
    d = {"price50":price100}
    return render(request,'carprice_filter2.html',d)
def CAR_PRICE3(request):
    price200 = [p for p in cars.objects.all() if (p.price >= 200000 and p.price <=300000)]
    d = {"price50":price200}
    return render(request,'carprice_filter3.html',d)
def CAR_PRICE4(request):
    price500 = [p for p in cars.objects.all() if (p.price >= 300000 and p.price <=5000000)]
    d = {"price50":price500}
    return render(request,'carprice_filter4.html',d)

######## DYNAMIC URLS   ########

def CAR_SINGLE(request,car_id):
    carss = cars.objects.get(id=car_id)
    ca  = cars.objects.all()
    caaa = ca[:3]
    d = {"carss":carss,"caaa":caaa}
    return render(request, 'car_detail.html',d)

def CAR_CATEGORY_FILTER(request,car_id):
    single = Carcategory.objects.get(id=car_id)
    carsingle = cars.objects.filter(category=single)
    d = {"carsingle":carsingle}
    return render(request, 'car_category_filter.html',d)

def CAR_PRICE(request,car_id):
    single = Carcategory.objects.get(id=car_id)
    carsingle = cars.objects.filter(category=single)
    d = {"carsingle":carsingle}
    return render(request, 'car_category_filter.html',d)