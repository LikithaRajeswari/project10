from django.shortcuts import render

# Create your views here.


def data_render(request):
    d={'name':'VARMA','age':4}
    return render(request,'data_render.html',context=d)

def conditions(request):
    d={'a':100,'b':200,'c':600,'hobbies':['drawing,crafting']}
    return render(request,'conditions.html',context=d)

def conditions1(request):
    d={'a':120,'b':220,'c':320}
    return render(request,'conditions1.html',context=d)

def conditions2(request):
    d={'s':250,'b':350,'c':450}
    return render(request,'conditions2.html',context=d)



