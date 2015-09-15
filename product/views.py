from django.shortcuts import render, render_to_response
from .models import Product
# Create your views here.
def show(request):
	products = Product.objects.all()
	return render_to_response('show.html',{'products':products'})
    

