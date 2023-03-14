from django.urls import path
from BackEnd import views

urlpatterns = [
    path('indexpg/',views.indexpg,name='indexpg'),
    path('adminpg/',views.adminpg,name='adminpg'),
    path('adminsave/',views.adminsave,name='adminsave'),
    path('displayadmin/',views.displayadmin,name='displayadmin'),
    path('editadmin/<int:dataid>/',views.editadmin,name='editadmin'),
    path('updateadmin/<int:dataid>/',views.updateadmin,name='updateadmin'),
    path('deletedata/<int:dataid>/',views.deletedata,name='deletedata'),
    path('categorypg/',views.categorypg,name='categorypg'),
    path('categorysave/',views.categorysave,name='categorysave'),
    path('displaycategory/',views.displaycategory,name='displaycategory'),
    path('editcategory/<int:dataid>/',views.editcategory,name='editcategory'),
    path('updatecategory/<int:dataid>/',views.updatecategory,name='updatecategory'),
    path('deletecategory/<int:dataid>/',views.deletecategory,name='deletecategory'),
    path('productpage/',views.productpage,name='productpage'),
    path('productsave/',views.productsave,name='productsave'),
    path('displayproduct/',views.displayproduct,name='displayproduct'),
    path('editproduct/<int:dataid>/',views.editproduct,name='editproduct'),
    path('updateproduct/<int:dataid>/',views.updateproduct,name='updateproduct'),
    path('deleteproduct/<int:dataid>/',views.deleteproduct,name='deleteproduct'),
    path('loginpg/',views.loginpg,name='loginpg'),
    path('loginadmin',views.loginadmin,name='loginadmin'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('displaycontact/',views.displaycontact,name='displaycontact'),
    path('deletemessage/<int:dataid>/',views.deletemessage,name='deletemessage')
]