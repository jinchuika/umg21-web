from .models import Cliente, Vehiculo
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cliente_form.html'
    fields = '__all__'
    success_url = 'cliente'
