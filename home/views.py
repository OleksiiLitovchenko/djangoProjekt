from django.shortcuts import render
from .models import PortfolioItem, About, Team


# Create your views here.
def view_homepage(request):
    portfolioitem = PortfolioItem.objects.filter(is_visible=True)
    abouts = About.objects.filter(is_visible=True)
    return render(request, 'index.html', context={'portfolioitem': portfolioitem, 'about': abouts })
