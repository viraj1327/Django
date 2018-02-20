from django.shortcuts import render

def base(request):
    '''
    Renders home page
    '''
    context = {}
    return render(request, 'base.html', context,)

def contact(request):
    '''
    Renders home page
    '''
    context = {}
    return render(request, 'contact.html', context,)

def portfolio(request):
    '''
    Renders home page
    '''
    context = {}
    return render(request, 'portfolio.html', context,)

def resume(request):
    '''
    Renders home page
    '''
    context = {}
    return render(request, 'resume.html', context,)

def home(request):
    '''
    Renders home page
    '''
    context = {}
    return render(request, 'home.html', context,)
