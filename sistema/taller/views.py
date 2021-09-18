from django.urls.base import reverse
from .models import Cliente, Vehiculo
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView)


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


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'cliente_form.html'
    fields = '__all__'
    success_url = 'cliente'

    def get_success_url(self):
        return reverse('cliente_detail', kwargs={'pk': self.kwargs['pk']})


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_delete.html'
    fields = '__all__'
    success_url = 'cliente'

    def get_success_url(self):
        return reverse('cliente_list')
