from django.shortcuts import render
from django.http import HttpResponse
from .models import PortfolioItem


# Create your views here.
def view_homepage(request):
    portfolioitem = PortfolioItem.objects.filter(is_visible=True)
    return render(request, 'index.html', context={'portfolioitem': portfolioitem})
