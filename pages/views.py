from django.shortcuts import render
from django.http import HttpResponse
from retailors.models import Retailor
from listings.models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices


# Create your views here.
def index(request):
	listings=Listing.objects.order_by('-list_data').filter(is_published=True)[:3]
	context ={
        'listings': listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
    }
	return render(request,'pages/index.html',context)

def about(request):
	retailor=Retailor.objects.order_by('-hire_date')
	mvp_retailors=Retailor.objects.filter(is_mvp=True)
	context={
	'retailors':retailor,
	'mvp_retailors':mvp_retailors
	}
	return render(request,'pages/about.html',context)

 