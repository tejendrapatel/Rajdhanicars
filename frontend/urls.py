
from django.contrib import admin
from django.urls import path
from zbikeapp.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include

urlpatterns = [
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('admin/', admin.site.urls),
    path('',VERIFICATION,name= 'verification'),
    path('verification_otp',VERIFICATION_OTP,name='verification_otp'),
    path('home', HOME , name = 'home'),
    path('contact/', CONTACT , name = 'contact'),
    path('about/', ABOUT , name = 'about'),
    path('bikes/', BIKES , name = 'bikes'),
    path('services', SERVICES , name = 'services'),
    path('pricing', PRICING , name = 'pricing'),
    path('terms_conditions',TERMS_CONDITIONS,name= 'terms_conditions'),
    path('privacy_policy',PRIVACY_POLICY,name= 'privacy_policy'),
    path('paymrnt_procedure',PAYMENT_PROCEDURE,name= 'payment_procedure'),
    path('buying_tips',BOOKING_TIPss,name= 'buying_tips'),
    path('faqs',FAQS,name= 'faqs'),
  
   
    path('carprice1',CAR_PRICE1, name='carprice1'),
    path('carprice2',CAR_PRICE2, name='carprice2'),
    path('carprice3',CAR_PRICE3, name='carprice3'),
    path('carprice4',CAR_PRICE4, name='carprice4'),

    #######dynamic urls ##########

    path('car_single/<int:car_id>/',CAR_SINGLE, name='car_single'),
    path('car_category_filter/<int:car_id>/',CAR_CATEGORY_FILTER, name='car_category_filter'),
 
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
