from django.views.generic import ListView, DetailView
from .models import Foods

class FoodListView(ListView):
    model = Foods
    template_name = 'food/food_list.html'
    context_object_name = 'food'
    ordering = ['-pk']

class FoodDetailView(DetailView):
    model = Foods
    template_name = 'food/food_detail.html'
    context_object_name = 'food'
