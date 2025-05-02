from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Category,Shirt,CartItem
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def home(request):
    return render(request,'app\home.html')



def products(request):
    shirts = Shirt.objects.all() 
    context = {'shirts': shirts}  
    return render(request, 'app/products.html', context)

@csrf_exempt
def submit_order(request):
    if request.method == 'POST':
        name = request.POST.get('customerName')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        product_name = request.POST.get('productName')
        quantity = request.POST.get('qty')
        total_price = request.POST.get('total')

        # TODO: Save this data in a model like `Order` if needed

        print(f"Order placed: {name}, {mobile}, {product_name}, Qty: {quantity}, ₹{total_price}")
        
        return JsonResponse({'message': 'Order placed successfully!'})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)


def cart(request):
    return render(request,'app\cart.html')


def order(request):
    return render(request, 'app\order.html')

def details(request, Shirtid):
    product = get_object_or_404(Shirt, id=Shirtid)
    context = {'product': product} 
    return render(request, 'app\details.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        profile_pic = request.FILES.get('profile_pic')

        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'app/register.html', {'error': 'Username already exists'})
        
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            profile_pic=profile_pic
        )
        return redirect('login')
    
    return render(request, 'app/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('product')
        else:
            return render(request, 'app\login.html', {'error': 'Invalid credentials'})
        
    return render(request, 'app\login.html')
#   product = get_object_or_404(product, id=productid)
#   return render(request, 'app\details.html', {'product': product})
    



# Create your views here.
