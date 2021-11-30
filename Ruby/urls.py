from django.urls import path
from . import views

urlpatterns = [
  
    path('', views.shop,name='home'),#page
    path('shop', views.shop,name='shop'),#page
    path('cart', views.cart,name='cart'),#page
    path('about', views.about,name='about'),#page
    path('loginview', views.loginview,name='loginview'),#page
    path('signup', views.signup,name='signup'),#page
    
    path('account', views.account,name='account'),#page
    path('checkout', views.checkout,name='checkout'),#page
    path('logoutview', views.logoutview,name='logoutview'),#page
    # path('increase_quan', views.increase_quan,name='increase_quan'),#page
    path('decrease_quan', views.decrease_quan,name='decrease_quan'),#page
    path('updatedetails/<int:user_id>', views.updatedetails,name='updatedetails'),#action
    path('updatecart', views.updatecart,name='updatecart'),#action
    path('add_to_cart/<int:product_id>', views.add_to_cart,name='add_to_cart'),#action
    # path('update_item/', views.updateItem,name="update_item"),
    
    
]