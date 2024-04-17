from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def entry_page(request):
    return HttpResponse('hello vishnu come back to django')
