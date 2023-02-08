from django.http import JsonResponse
from django.shortcuts import render,redirect
# from django.conf import settings
from customer.models import Customer
from owner.models import Mobile
from customer.models import Order

# from commen.models import ustomer 
# Create your views here.


def home_page(request):
    mobile_list = Mobile.objects.all()
    if request.method == 'POST':
        mobileid=int(request.POST['mid'])
        print(mobileid)
        order = Order(
                customer_id = request.session['customer'],
                mobile_details_id = mobileid
            )
        order.save()
    return render(request,'customer/view_products.html',{'mobile_list':mobile_list})

def login_cus(request):
    msg = ''
    if request.method == 'POST' :
        print('test')
        username = request.POST['c-user-name']
        password = request.POST['c-password']
        try :
            customer = Customer.objects.get(
            username = username,
            password = password
            )
            request.session['customer'] = customer.id
            return redirect('customer:home-page')
        except :
            msg = 'Invalid Password Or Username'
    return render(request,'customer/login.html',{'msg':msg})

def register_cus(request):
    msg = ''
    if request.method == 'POST':
        cus_name = request.POST['cus_name']
        cus_email = request.POST['email']
        cus_phone = request.POST['cus_phone']
        cus_username = request.POST['cus_username']
        cus_password = request.POST['password']
    
        customer01 = Customer(
            name = cus_name,
            email = cus_email ,
            contact_no = cus_phone,
            username = cus_username,
            password = cus_password)
        customer01.save()
        msg = 'registred succesfully'
    return render(request,'customer/register.html',{'msg':msg})

# def purchase(request):
#     if request.method == 'POST':
#         mobileid=int(request.POST['mid'])
#         print(mobileid)
#         order = Order(
#                 customer_id = request.session['customer'],
#                 mobile_details_id = mobileid
#             )
#         order.save()
#     return redirect( 'customer:home-page' )
