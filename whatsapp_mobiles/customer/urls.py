from django.urls import path
from . import views
app_name='customer'

urlpatterns = [
    path('',views.login_cus,name='login-cus'),
    path('home',views.home_page,name='home-page'),
    path('register',views.register_cus,name='register-cus'),
    # path('purchase/<int:mobileid>',views.purchase,name='purchase-req'),
   
]