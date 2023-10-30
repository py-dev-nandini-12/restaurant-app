from django.shortcuts import render
from django.views import generic

from resturant_menu.models import Item,MEAL_TYPES


# Create your views here.
class MenuList(generic.ListView):
    queryset = Item.objects.order_by("date_created")
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPES
        return context


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = 'menu_item_detail.html'