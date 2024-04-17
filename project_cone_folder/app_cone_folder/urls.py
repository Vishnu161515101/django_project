from django.urls import path
from  . import views


urlpatterns = [
    path('entry_page',views.entry_page,name='entry_page')
   
]
