from django.shortcuts import render

from django.views.generic import ListView, DetailView, UpdateView

from django.core.urlresolvers import reverse

from .models import Year, SubYear, Income

class IncomeListView(ListView):
    model = Income
    template_name = 'fees/income_list_simple.html'
    context_object_name = "income_list"
    paginate_by = 10

