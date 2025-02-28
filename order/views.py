from re import I
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from . import models, forms
from .forms import OrderForm
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache

# списка заказов 
@method_decorator(cache_page(60*15), name='dispatch')
class OrderListView(generic.ListView):
    template_name = 'order/order_list.html'
    context_object_name = 'order_lst'
    model = models.OrderModel

    def get_queryset(self):
        orders = cache.get('orders')
        if not orders:
            orders = self.model.objects.all().order_by('-id')
            cache.set('orders', orders, 60*15)
        return orders


#  деталей заказа
@method_decorator(cache_page(60*10), name='dispatch')
class OrderDetailView(generic.DetailView):
    model = models.OrderModel
    template_name = 'order/order_detail.html'
    context_object_name = 'order'


# создания заказа
class CreateOrderView(generic.CreateView):
    template_name = 'order/create_order.html'

    def get(self, request):
        form = OrderForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            cache.delete('orders')  
            return redirect('order_lst')
        return render(request, self.template_name, {'form': form})


# удалении заказа
class DeleteOrderView(generic.DetailView):
    def get(self, request, id):
        order = get_object_or_404(models.OrderModel, id=id)
        order.delete()
        cache.delete('orders')  
        return redirect('order_lst')


# обновлении заказа
class UpdateOrderView(generic.UpdateView):
    def get(self, request, id):
        order = get_object_or_404(models.OrderModel, id=id)
        form = forms.OrderForm(instance=order)
        return render(request, 'order/update_order.html', {'form': form, 'order_id': order})

    def post(self, request, id):
        order = get_object_or_404(models.OrderModel, id=id)
        form = forms.OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            cache.delete('orders') 
            cache.delete(f'order_{id}')  
            return redirect('order_lst')
        return render(request, 'order/update_order.html', {'form': form, 'order_id': order})
