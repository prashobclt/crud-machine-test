from django.urls import path
from . import views
app_name='owner'

urlpatterns = [
    path('master',views.master_page,name='master-page'),
    path('login',views.login,name='login-page'),
    path('add_mobile',views.add_mobile,name='add-mobile'),
    path('manage_products',views.manage_products,name='manage-products'),
    path('purchase_req',views.purchase_req,name='purchase-req'),
    path('registred_cus',views.registred_cus,name='registred-cus'),
    # path('update/<int:mobileid>',views.mobile_update,name='m-update'),
    path('delete/<int:mobileid>',views.mobile_delete,name='m-delete')
    
]