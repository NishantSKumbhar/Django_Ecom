from django.shortcuts import render
from .models import Product, Discount
def home(request):
	product = Product.objects.all()
	discount = Discount.objects.all()
	context = {
		'products' : product,
		'discount' : discount,
		'title' : 'Home - Lexcrop'
	}

	return render(request, 'products/home.html', context)

def about(request):
	context = {
		'title' : 'About - Lexcrop'
	}

	return render(request, 'products/about.html', context)

def contact(request):
	context = {
		'title' : 'Contact - Lexcrop'
	}

	return render(request, 'products/contact.html', context)