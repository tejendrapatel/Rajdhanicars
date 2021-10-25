from pdb import set_trace
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
from frontend.settings import account_sid,auth_token,my_twilio
from twilio.rest import Client
def LOGIN(request):
    error = False
    if request.method == "POST":
        d = request.POST
        u = d['usr']
        p = d['pass']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('admin_index')
        else:
            error = True
    d = {'error': error}
    return render(request, "login.html", d)

def FORGOT(request):
    error = False
    form = False
    udata = False
    if request.method == "POST":
        dd = request.POST
        name = dd["form"]
        if name == "submit email":
            e = dd['em']
            user = User.objects.filter(email = e)
            if user:
                form = True
                udata = user[0]
            else:
                error = True
        if name == 'submit pwd':
            p = dd ['pwd']
            c = dd ['cpwd']
            u = dd ['idd']
            user = User.objects.get(id=u)
            user.set_password(p)
            user.save()
            return redirect ('Login')
    d = {"form":form,"error":error,"udata":udata}
    return render(request,'forgot.html',d)

def LOGOUT(request):
    logout(request)
    return redirect('home')

def VERIFICATION(request):
    if request.method == "POST":
        f = request.POST
        namee = f['nam']
        emaii = f['ema']
        mobb = f['mob']
        co = f['cod']
        my_cell= co+mobb 
        ra=random.randint(1000,9999)
        temp=ra
        client = Client(account_sid, auth_token)
        my_msg = ' "you are succesfully registered in Authenticator your security code is "{}" '.format(temp)
        message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
        subject = "Congratulation "
        content = ' "you are succesfully registered in Authenticator your security code is "{}" '.format(temp)
        msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{emaii}'])
        msg.send()
       
        Verifications.objects.create(name=namee, email=emaii, mobile=mobb, temporary = temp)
        return redirect('verification_otp')
    return render(request,'verification.html')

def VERIFICATION_OTP(request):
    if request.method == "POST":
        f = request.POST
        namees = f['zzz']
        if Verifications.objects.filter(temporary=namees).exists():
            return redirect('home')
        else:
            return redirect('verification')
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
    clientss = happy_clients.objects.all()
    fclientss = fcli.objects.all()
    ban = MAIN_BANNER.objects.all().order_by('-id')
    banner = ban[:1]
    d = {"ca":ca,"carr":carr,"price50":price50,"price100":price100,"price200":price200,"price500":price500,"fclientss":fclientss,"clientss":clientss,"you":you,"you2":you2,'banner':banner}
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
    carssz = cars.objects.get(id=car_id)
    ca  = cars.objects.all()
    caaa = ca[:3]
    if request.method == "POST":
        f = request.POST
        tname = f['name']
        temai = f['email']
        tmob = f['mobi']
        tdat = f['dat']
        ttim = f['tim']
        tmsg = f['message']
        testdrive.objects.create(name=tname, email=temai, mobile=tmob, message=tmsg,date=tdat,time=ttim)
    d = {"carssz":carssz,"caaa":caaa}
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

###########      admin pannel        ########

def ADMIN_YOUTUBE(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        return render(request, 'admin/admin_youtube.html')
####site visitor  ####
def ADMIN_SITEVISITOR(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        con = Verifications.objects.all()
        d = {"con":con}
        return render(request, 'admin/admin_sitevisitor.html',d)
#########contact  #####  
def ADMIN_CONTACT(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        con = Contact.objects.all()
        d = {"con":con}
        return render(request, 'admin/admin_contact.html',d)
#######finincial banks patners####
def ADMIN_GALLERY(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            campna = request.FILES['cam']
            fcli.objects.create(image=campna)
        fir = fcli.objects.all()
        d = {"fir": fir}
        return render(request, 'admin/admin_finincialclients.html',d)
########happy clients ####
def ADMIN_NEWS(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            campna = request.FILES['cam']
            happy_clients.objects.create(image=campna)
        fir = happy_clients.objects.all()
        d = {"fir": fir}
        return render(request, 'admin/admin_happyclients.html',d)
#######car category ##
def ADMIN_CAR_CATEGORY(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            campna = request.FILES['cam']
            namee = request.POST['nam']
            Carcategory.objects.create(image=campna,name=namee)
        fir = Carcategory.objects.all()
        d = {"fir":fir}
        return render(request, 'admin/admin_car_category.html',d)
########add car#####
def ADMIN_CAR(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        ca= Carcategory.objects.all()
        if request.method == "POST":
            g = request.POST
            ccbrand = g['cbrand']
            carbrand = Carcategory.objects.get(name=ccbrand)
            ccname = g['cname']
            varr=g['vart']
            ccmodel = g['cmodel']
            ccpetrol = g['cyear']
            cckilometer = g['ckilometer']
            cccolour = g['ccolour']
            ccregistration = g['cregistration']
            ccregisno = g['cregno']
            ccinsurance = g['cinsurance']
            ccowner = g['cowner']
            ccprice = g['cprice']
            ccdetail = g['cdetail']
            ccimg1 = request.FILES ['cimga']
            ccimg2 = request.FILES ['cimg2']
            ccimg3 = request.FILES ['cimg3']
            ccimg4 = request.FILES ['cimg4']
            ccimg5 = request.FILES ['cimg5']
            ccimg6 = request.FILES ['cimg6']
            ccimg7 = request.FILES ['cimg7']
            ccimg8 = request.FILES ['cimg8']
            ccimg9 = request.FILES ['cimg9']
            cars.objects.create(varient=varr,category=carbrand,name=ccname,model=ccmodel,fuel_type=ccpetrol,kilometer=cckilometer,
            colour=cccolour,registration_type=ccregistration,registration_No=ccregisno,Insurance=ccinsurance,owners=ccowner,price=ccprice,
            discription=ccdetail,image=ccimg1,image2=ccimg2,image3=ccimg3,image4=ccimg4,image5=ccimg5,image6=ccimg6,
            image7=ccimg7,image8=ccimg8,image9=ccimg9)
        d = {"ca":ca}
        return render(request, 'admin/admin_car_add.html',d)

#####admin test drive###
def ADMIN_TEST_DRIVE(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        con = testdrive.objects.all().order_by('-id')
        d = {"con":con}
        return render(request,'admin/admin_testdrive.html',d)
######admin add banner###
def ADMIN_ADD_BANNER(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            campn1 = request.FILES['ban1']
            campn2 = request.FILES['ban2']
            campn3 = request.FILES['ban3']
            MAIN_BANNER.objects.create(aimage=campn1,bimage=campn2,cimage=campn3)
        return render(request,'admin/admin_add_banner.html')
######alll cars###
def ADMIN_ALL_CARS(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        con = cars.objects.all()
        d = {"con":con}
        return render(request,'admin/admin_all_cars.html',d)


def ADMIN_INDEX(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        vis = Verifications.objects.all().order_by('-id')
        vist= vis[:10]
        test = testdrive.objects.all().order_by('-id')
        tes= test[:10]
        contact = Contact.objects.all().order_by('-id')
        con  = contact[:10]
        d = {"vist":vist,"tes":tes,"con":con}
        return render(request, 'admin/admin_index.html',d)





#####     admin delete ####

def ADMIN_GALLERY_DELETE(request,del_id):
    fcli.objects.get(id=del_id).delete()
    return redirect('admin_gallery')

def ADMIN_NEWS_DELETE(request,del_id):
    happy_clients.objects.get(id=del_id).delete()
    return redirect('admin_news')

def ADMIN_CAR_DELETE(request,del_id):
    Carcategory.objects.get(id=del_id).delete()
    return redirect('car_category')


def ADMIN_ALLCAR_DELETE(request,del_id):
    cars.objects.get(id=del_id).delete()
    return redirect('admin_all_cars')