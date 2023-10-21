from django.shortcuts import render
from .models import PortfolioItem


# Create your views here.
def view_homepage(request):
    portfolioitem = PortfolioItem.objects.filter(is_visible=True)
    return render(request, 'main.html', context={'portfolioitem': portfolioitem})
