from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Product
# Create your views here.
def home_view(request,*args,**kwargs):
    obj = Product.objects.all()
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,"dd.html",{'obj':obj})

def product_detail_view(request,id):
    try:
         obj = Product.objects.get(id=id)

    except Product.DoesNotExist:
       raise Http404

    
    return HttpResponse(f"product id {obj.id}") 

def product_api_detail(request,*args,**kwargs):

    obj = Product.objects.all()
    
    return JsonResponse({"id":obj.id})    
