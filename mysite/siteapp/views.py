from django.shortcuts import render
from .models import Numbers


# Create your views here.

def index(request):
    return render(request, 'index.html')

def numbers(request):
    nums = Numbers.objects.all().order_by('value')
    data = {'nums': nums}
    # data = {'numbers': [1, 2, 3, 4]}
    return render(request, 'numbers.html', data)
 
