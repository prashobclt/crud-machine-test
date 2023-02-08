from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.conf import settings 
from owner.models import Owner,Mobile
from customer.models import Customer,Order

# Create your views here.
def master_page(request):
    return render(request,'owner/master_page.html')

def login(request):
    msg = ''
    if request.method == 'POST' :
        print('test')
        username = request.POST['o-user-name']
        password = request.POST['o-password']
        try :
            owner = Owner.objects.get(
            name = username,
            password = password
            )
            request.session['owner_id'] = owner.id
            return redirect('owner:manage-products')
        except :
            msg = 'Invalid Password Or Username'
    return render(request,'owner/login.html',{'msg':msg})

def add_mobile(request):
    msg = ""
    if request.method == 'POST':
        m_name = request.POST['Model-name']
        m_brand = request.POST['brand']
        m_rate = request.POST['rate']
        m_image = request.FILES['image']
        mobile01 = Mobile(
            mobile_name = m_name,
            mobile_brand = m_brand,
            mobile_rate = m_rate,
            mobile_image = m_image
        )
        mobile01.save()
        msg = "Mobile Added Succesfully"
    return render(request,'owner/add_mobile.html',{'msg':msg})

def manage_products(request):
    prod_list = Mobile.objects.all()
    if request.method == 'POST':
        mobileid =int(request.POST['mid'])
        print(mobileid)
            
        u_name = request.POST['u-name']
        u_brand = request.POST['u-brand']
        u_rate = float(request.POST['u-rate'])
        u_image = request.FILES['u-image']  

        u_product = Mobile.objects.filter(id = mobileid).update(mobile_name = u_name,
            mobile_brand = u_brand,
            mobile_rate = u_rate,
            mobile_image = u_image)
    return render(request,'owner/manage_products.html',{'product_list':prod_list})

def purchase_req(request):
    order_list = Order.objects.all()
    return render(request,'owner/purchase_req.html',{'order_list':order_list})

def registred_cus(request):
    reg_customer = Customer.objects.all()
    return render(request,'owner/registred_customer.html',{'cus_list':reg_customer})

def mobile_update(request,mobileid):
    update_mobile = Mobile.objects.filter(
        id = mobileid)
    update_mobile.update()
    return redirect('owner:manage-products')

def mobile_delete(request,mobileid):
    delete_mobile = Mobile.objects.filter(
        id = mobileid)
    delete_mobile.delete()
    return redirect('owner:manage-products')