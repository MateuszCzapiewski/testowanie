from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import CarList
from .models import Book

def car_list(request):
    cars = CarList.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

class BookDetailView(DetailView):
    model=Book
    template_name='ai_app/book_detail.html'
    context_object_name='book'