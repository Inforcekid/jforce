from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('frontend/index.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('frontend/about.html')
    return HttpResponse(template.render())


def classes(request):
    template = loader.get_template('frontend/classes.html')
    return HttpResponse(template.render())


def portfolio(request):
    template = loader.get_template('frontend/portfolio.html')
    return HttpResponse(template.render())


def shop(request):
    template = loader.get_template('frontend/shop.html')
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template('frontend/contact.html')
    return HttpResponse(template.render())


def portfolio_details(request):
    template = loader.get_template('frontend/portfolio-details.html')
    return HttpResponse(template.render())
