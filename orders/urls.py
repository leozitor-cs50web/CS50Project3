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
    path('additem/<str:category>/<str:name>/<str:price>', views.add_item, name='additem'),
    path('removeitem/<str:item_id>', views.remove_item, name='removeitem')
]
