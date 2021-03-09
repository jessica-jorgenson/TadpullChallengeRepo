import random
import string

from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View

from .models import Item


def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))


""" def products(request):
    myFilter = ProductFilter(request.GET,queryset=Item.objects.all())
    items = myFilter.qs
    context = {
        'items': items
    }
    return render(request, "products.html", context) """


class HomeView(ListView):
    model = Item
    paginate_by = 12
    template_name = "home.html"

"""     def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['filter'] = ItemFilter(
                self.request.GET, queryset=self.get_queryset())
            return context """


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"

""" class FilterView(ListView):
    model = Item
    paginate_by = 12
    template_name = "filter.html"
    
    def get_queryset(self):
        # original qs
        query = self.request.GET['category']
        
        # filter by a variable captured from url, for example
        filter = Item.objects.filter(brand_id=int(query))
        return filter """
