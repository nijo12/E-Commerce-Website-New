from django.urls import path
from Frontend import views

urlpatterns = [
    path('',views.homepg,name='homepg'),
    path('aboutpg/',views.aboutpg,name='aboutpg'),
    path('contactpg/',views.contactpg,name='contactpg'),
    path('productpg/<itemCatg>', views.productpg, name='productpg'),
    path('productsinglepg/<int:dataid>',views.productsinglepg,name='productsinglepg'),
    path('registerloginpg/', views.registerloginpg, name='registerloginpg'),
    path('registersave/',views.registersave,name='registersave'),
    path('customerlogin/',views.customerlogin,name='customerlogin'),
    path('customerlogout/', views.customerlogout, name='customerlogout'),
    path('contactsave/',views.contactsave,name='contactsave'),
    path('cartpg/<int:dataid>',views.cartpg,name='cartpg'),

]