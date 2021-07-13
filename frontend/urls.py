
from django.contrib import admin
from django.urls import path
from zbikeapp.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include

urlpatterns = [
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('admin/', admin.site.urls),
    path('', HOME , name = 'home'),
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

    path('car_single/<int:car_id>/',CAR_SINGLE, name='car_single'),
    path('car_category_filter/<int:car_id>/',CAR_CATEGORY_FILTER, name='car_category_filter'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
