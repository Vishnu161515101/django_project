from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def entry_page(request):
    return HttpResponse('hello vishnu come back to django')

def entry_page1(request):
   template = loader.get_template('entry_pages_for_cone.html')
   return HttpResponse(template.render())
