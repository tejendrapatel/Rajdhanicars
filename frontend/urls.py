
from django.contrib import admin
from django.urls import path
from zbikeapp.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include

urlpatterns = [
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('admin/', admin.site.urls),
    path('Logout/',LOGOUT,name='Logout'),
    path('Login/',LOGIN,name='Login'),
    path('Forgot/',FORGOT,name='Forgot'),
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

    #####       admin pannel   ##########
    path('admin_index',ADMIN_INDEX,name= 'admin_index'),
    path('admin_contact',ADMIN_CONTACT,name= 'admin_contact'),
    path('admin_car_category',ADMIN_CAR_CATEGORY,name= 'car_category'),
    path('admin_car',ADMIN_CAR,name= 'admin_cars'),
    path('admin_news', ADMIN_NEWS, name='admin_news'),
    path('admin_gallery', ADMIN_GALLERY, name='admin_gallery'),

    path('admin_youtube',ADMIN_YOUTUBE, name='admin_youtube'),
    path('admin_site_visitor',ADMIN_SITEVISITOR, name='admin_site_visitor'),
    path('admin_test_drive',ADMIN_TEST_DRIVE, name='admin_test_drive'),
    path('admin_add_banner',ADMIN_ADD_BANNER, name='admin_add_banner'),
    path('admin_all_cars',ADMIN_ALL_CARS, name='admin_all_cars'),

####  admin delete  ####
    path('admin_gallery_delete/<int:del_id>/', ADMIN_GALLERY_DELETE, name='admin_gallery_delete'),
    path('admin_news_delete/<int:del_id>/', ADMIN_NEWS_DELETE, name='admin_news_delete'),
    path('admin_car_delete/<int:del_id>/', ADMIN_CAR_DELETE, name='admin_car_delete'),
    path('admin_allcar_delete/<int:del_id>/', ADMIN_ALLCAR_DELETE, name='admin_allcar_delete'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
