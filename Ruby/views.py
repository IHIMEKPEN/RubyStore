#modules used
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *

# Create your views here.
#homepage
def home(request):
    if  request.user.is_authenticated :
        name=request.user.first_name
        context={
            "name": name,

         }
        return render(request,'ruby/index.html',context)
    else :
        return render(request,'ruby/index.html')

#page for shop
def shop(request):
    products=Product.objects.all()    

    if  request.user.is_authenticated :
        name=request.user.first_name
        length=0  
        if request.user.cart_list.all():
            length=len(request.user.cart_list.all()) 
        cart_list=request.user.cart_list.all()
                 
        context={
            "name": name,
            'products':products, 
            'cart_no':length,
            'items':cart_list,

         }
        return render(request,'ruby/shop.html',context)
    else :
        context={
            'products':products
        
        }
        return render(request,'ruby/shop.html',context)
  





#page for about
def about(request):
    context={

    }
    return render(request,'ruby/about.html',context)

#page for account
def account(request):
    name=request.user.first_name
    lastname=request.user.last_name
    email=request.user.email
    context={
        "name": name,
        "lastname": lastname,
        "email": email,

    }
    return render(request,'ruby/my-account.html',context)

def loginview(request):
    if request.method =="POST":        
        email=request.POST['email']          
        password=request.POST['password']           
        user = authenticate(request, username=email, password=password)
        
         # Check if authentication successful
        if user is not None:
            login(request,user)
            return redirect('shop')
        else:
            request.session['message'] = "Invalid email and/or password."
            return render(request,'ruby/login-register.html')
    else:
        return render(request, "ruby/login-register.html")
    
   
    

def signup(request):
    if request.method =="POST":        
        firstname=request.POST['firstname']   
        lastname=request.POST['lastname']   
        email=request.POST['email']   
        password=request.POST['password']   
        confirmation=request.POST['confirmation']   

        if password != confirmation:
            request.session['message'] = "Passwords must match."
            
            return render(request, "ruby/signup.html")

         # Attempt to create new user
        try:
            user = User.objects.create_user(first_name=firstname,last_name=lastname, password=password ,email=email ,username=email)
            user.save()
        except IntegrityError:
            request.session['message'] = "email already registered."
            return render(request, "ruby/signup.html")
        login(request,user)
        return redirect('shop')
    
    print('sign-up')
    return render(request, "ruby/signup.html")
        
    
  

def logoutview(request):
    logout(request)
    return redirect('loginview')



def blog(request):
    name=request.user.first_name 
    context={
        "name": name,

    }
    return render(request,'ruby/single-blog.html',context)

#handle functionaly of updating details
def updatedetails(request,user_id):
    user=User.objects.get(id=user_id)  
    print(user.first_name) 
    
    if request.method =="POST":     
        # user=User.objects.get(id=user_id)   
        firstname=request.POST['firstname']   
        lastname=request.POST['lastname'] 
        password=request.POST['password']   
        confirmation=request.POST['confirmation']  
        current_password=request.POST['current_password']        
        print(user.first_name)
        verify_user=user.check_password(current_password)
        # print(verify_user)
        if verify_user :
            if password != confirmation:
                request.session['message'] = 'Password mismatch.'
                return render(request, "ruby/my-account.html")
            else:
                user.first_name =firstname
                user.last_name =lastname
                # user.password =password 
                user.set_password(password)               
                user.save() 
                login(request,user)
                request.session['message'] = 'Account details updated Successfully.'

                return redirect ('account')
        else:
            request.session['message'] = "Incorrect Username and/or Password ."
           
        
            return render(request, "ruby/my-account.html")
        
#page for cart
def cart(request):
    if request.user.is_authenticated:
        name=request.user.first_name 
        cart_list=request.user.cart_list.all()
        length=0  
        if request.user.cart_list.all():
            length=len(request.user.cart_list.all())     

        # order,created = Order.objects.get_or_create(user=request.user,complete=False)#bcus we either want to 
        #create an order or get one if it exists
        items=cart_list
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        context={
            'items':cart_list,
            'cart_no':length,
            "name": name,
            }      
        return render(request,'ruby/cart.html',context)
   

   
    
@login_required
def add_to_cart(request,product_id):
    user=User.objects.get(id=request.user.id)  
    if request.method =="POST": 
        
        product=Product.objects.get(id=product_id)
        # print(type(user.cart_list))
        user.cart_list.add(product)
        
        length=len(user.cart_list.all())
        context={
            
            'cart_no':length,
            
            }
        return redirect ('shop')

@login_required
def remove_from_cart(request, product_id):
    pass
    
         


#page for checkout
def checkout(request):
    name=request.user.first_name
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}

    context={
        "name": name,
        'items':items,
        'order':order,
    }
    return render(request,'ruby/checkout.html',context)



def increase_quan(request):
    if request.method =="POST": 

        pass

def decrease_quan(request):
    if request.method =="POST": 
        pass



    