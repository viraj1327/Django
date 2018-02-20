from django.shortcuts import render
from .models import Education, Experience

# Create your views here.

def home(request):
    '''
    Renders the resume app home.html
    '''
    qsEx=Experience.objects.all()
    qsEdu=Education.objects.all()
    context={'experience':qsEx, 'education':qsEdu, 'Resume':'active'}
    return  render(request, 'Resume/home.html',context{})
