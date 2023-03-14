from django.shortcuts import render, redirect

from BackEnd.models import categorydb, productdb, contactdb
from Frontend.models import customerdb
from django.contrib import messages


def homepg(req):
    data = categorydb.objects.all()
    return render(req,"Home.html",{'data':data})
def aboutpg(req):
    data = categorydb.objects.all()
    return render(req,"About.html",{'data':data})
def contactpg(req):
    data = categorydb.objects.all()
    datas = contactdb.objects.all()
    return render(req,"Contact.html",{'data':data,'datas':datas})
def contactsave(request):
    if request.method == "POST":
        na = request.POST.get("name")
        em = request.POST.get("email")
        ph = request.POST.get("phone")
        msg = request.POST.get("msg")
        obj = contactdb(Name=na,Email=em,Phone=ph,Message=msg)
        obj.save()
        return redirect(contactpg)


def productpg(req, itemCatg):
    catg = itemCatg.upper()

    products = productdb.objects.filter(Category=itemCatg)
    data = categorydb.objects.all()
    context = {
        'data':data,
        'products' : products,
        'catg' : catg
    }
    return render(req,"product.html",context)

def productsinglepg(req,dataid):
    da = categorydb.objects.all()
    data = productdb.objects.get(id=dataid)
    return render(req,"productsingle.html",{'data':data,'da':da})
def registerloginpg(req):
    data = categorydb.objects.all()
    return render(req,"Register_or_Login.html",{'data':data})
def registersave(request):
    if request.method == "POST":
        na = request.POST.get("name")
        em = request.POST.get("email")
        pas = request.POST.get("pass")
        con = request.POST.get("confirm")
        if pas == con:
            obj = customerdb(User_Name=na,Email=em,Password=pas,Confirm_Password=con)
            obj.save()
            messages.success(request, "register successfully")
            return redirect(registerloginpg)
        else :
            return render(request, "Register_or_Login.html", {'msg1': "sorry password not matched"})



def customerlogin(request):
    if request.method == "POST":
        username_r = request.POST.get("user")
        password_r = request.POST.get("pass")
        if customerdb.objects.filter(User_Name=username_r,Password=password_r).exists():
            request.session['user']=username_r
            request.session['pass']=password_r
            messages.success(request, "login successfully")

            return redirect(homepg)
        else:
            messages.error(request, "invalid user")
            return render(request, "Register_or_Login.html")

def customerlogout(request):
    del request.session['user']
    del request.session['pass']
    messages.success(request, "logout successfully")
    return redirect(homepg)

def cartpg(req,dataid):
    da = categorydb.objects.all()
    datas = productdb.objects.get(id=dataid)

    return render(req,"Cart.html",{'datas':datas,'da':da})


