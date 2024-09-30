from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
import math

# Create your views here.

def Observer_page(request):
   object_on_page = int(request.GET.get('object_on_page', '3'))
   if request.method == 'POST':
      object_on_page = int(request.POST.get('page_numbers'))

   games = Game.objects.all()
   paginator = Paginator(games, object_on_page)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   number_of_pages = math.ceil(len(games)/object_on_page)
   context = {'page_obj': page_obj, 'object_on_page': object_on_page, 'number_of_pages': number_of_pages}
   return render(request, 'observer_page.html', context)



