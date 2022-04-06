from django.shortcuts import render
from .models import Product

def home(request):
	product = Product.objects.all()
	context = {
		'products' : product,
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