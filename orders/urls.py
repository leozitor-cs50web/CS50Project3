from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('additem/<str:category>/<str:name>/<str:price>/<str:size>', views.add_item, name='additem'),
    path('removeitem/<str:item_id>/<str:option>', views.remove_item, name='removeitem'),
    path('shoppingcart/', views.shoppingcart, name='shoppingcart'),
    path('checkout/', views.checkout, name='checkout'),
    path('addtopping/', views.add_topping, name='addtopping'),
    path('sucess/', views.sucess, name='sucess'),
    path('orders/<int:order_page>', views.orders, name='orders'),
    path('adminorders/<str:order_type>/<int:order_page>', views.adminorders, name='adminorders')
]
