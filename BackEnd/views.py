from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from BackEnd.models import admindb, categorydb, productdb, contactdb
from django.contrib import messages

def indexpg(req):
    return render(req,"index.html")
def adminpg(req):
    return render(req,"AddAdmin.html")
def adminsave(request):
    if request.method == "POST":
        na = request.POST.get("name")
        em = request.POST.get("email")
        nb = request.POST.get("number")
        us = request.POST.get("user")
        pa = request.POST.get("pass")
        co = request.POST.get("confirm")
        im = request.FILES["img[]"]
        obj = admindb(Name=na, Email=em, Mob_No=nb, User_Name=us, Password=pa, Confirm_Password=co, Image=im)
        obj.save()
        messages.success(request, "Admin Added Successfully")
        return redirect(adminpg)

def displayadmin(req):
    data = admindb.objects.all()
    return render(req,"DisplayAdmin.html",{'data':data})
def editadmin(req,dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(req,"EditAdmin.html",{'data':data})


def updateadmin(request,dataid):
    if request.method == "POST":
        na = request.POST.get("name")
        em = request.POST.get("email")
        cn = request.POST.get("number")
        us = request.POST.get("user")
        pa = request.POST.get("pass")
        ne = request.POST.get("confirm")
        try :
            im = request.FILES["img[]"]
            fs = FileSystemStorage()
            file = fs.save(im.name,im)
        except MultiValueDictKeyError :
            file = admindb.objects.get(id=dataid).Image
        admindb.objects.filter(id=dataid).update(Name=na,Email=em,Mob_No=cn,User_Name=us,Password=pa,Confirm_Password=ne,Image=file)
        messages.success(request, "Update Successfully")
        return redirect(displayadmin)

def deletedata(req,dataid):
    data = admindb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Deleted")
    return redirect(displayadmin)

def categorypg(req):
    return render(req,"AddCategory.html")
def categorysave(request):
    if request.method == "POST":
        ca = request.POST.get("name")
        de = request.POST.get("text")
        im = request.FILES["img[]"]
        obj = categorydb(Category_Name=ca,Description=de,Image=im)
        obj.save()
        messages.success(request, "Category Added Successfully")
        return redirect(categorypg)

def displaycategory(req):
    data = categorydb.objects.all()
    return render(req,"DisplayCategory.html",{'data':data})

def editcategory(req,dataid):
    data = categorydb.objects.get(id=dataid)
    print(data)
    return render(req,"Editcategory.html",{'data':data})
def updatecategory(request,dataid):
    if request.method == "POST":
        na = request.POST.get("name")
        tx = request.POST.get("text")
        try:
            im = request.FILES["img[]"]
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).Image
        categorydb.objects.filter(id=dataid).update(Category_Name=na,Description=tx,Image=file)
        messages.success(request, "Update Successfully")
        return redirect(displaycategory)

def deletecategory(req,dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Deleted")
    return redirect(displaycategory)


def productpage(req):
    data = categorydb.objects.all()
    return render(req,"Addproduct.html",{'data':data})
def productsave(request):
    if request.method == "POST":
        ca = request.POST.get("category")
        pr = request.POST.get("product")
        pi = request.POST.get("price")
        qu = request.POST.get("quantity")
        de = request.POST.get("des")
        im = request.FILES["img[]"]
        obj = productdb(Category=ca,Product_Name=pr,Price=pi,Quantity=qu,Description=de,Image=im)
        obj.save()
        messages.success(request, "Product Added Successfully")
        return redirect(productpage)

def displayproduct(req):
    data = productdb.objects.all()
    return render(req,"DisplayProduct.html",{'data':data})
def editproduct(req,dataid):
    data = productdb.objects.get(id=dataid)
    da = categorydb.objects.all()
    print(data)
    return render(req,"EditProduct.html",{'data':data, 'da':da})
def updateproduct(request,dataid):
    if request.method == "POST":
        ca = request.POST.get("category")
        pr = request.POST.get("product")
        pi = request.POST.get("price")
        qu = request.POST.get("quantity")
        de = request.POST.get("des")
        try:
            im = request.FILES["img[]"]
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(Category=ca,Product_Name=pr,Price=pi,Quantity=qu,Description=de,Image=file)
        messages.success(request, "Update Successfully")
        return redirect(displayproduct)

def deleteproduct(req,dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Deleted")
    return redirect(displayproduct)

def loginpg(req):
    return render(req,"login.html")
def loginadmin(request):       # doesn't want to create database, because it is an super user already will be stored as built in
    if request.method == "POST":
        username_r = request.POST.get('user')
        password_r = request.POST.get('pass')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request,user)
                request.session['user']=username_r
                request.session['pass']=password_r
                messages.success(request, "Login Successfully")
                return redirect(indexpg)
            else:
                return redirect(loginpg)
        else:
            return redirect(loginpg)

def adminlogout(request):
    del request.session['user']
    del request.session['pass']
    messages.success(request, "Logout Successfully")
    return redirect(loginpg)

def displaycontact(req):
    datas = contactdb.objects.all()
    return render(req,"DisplayWebsiteContact.html",{'datas':datas})
def deletemessage(req,dataid):
    datas = contactdb.objects.filter(id=dataid)
    datas.delete()
    messages.success(req, "Deleted")
    return redirect(displaycontact)
