from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from .forms import CarForm
from .models import Car


# Create your views here.
class CarCreate(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'create_car.html'
    success_url = reverse_lazy('list')
    
class CarList(ListView):
    model = Car
    template_name = 'list_cars.html'
    context_object_name = 'cars'
    
class CarDelete(DeleteView):
    model = Car
    pk_url_kwarg = 'car_id'
    template_name = 'delete_car.html'
    success_url = reverse_lazy('list')