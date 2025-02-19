from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from . import models, forms
from .forms import OrderForm

#весь список
class OrderListView(generic.ListView):
    template_name = 'order/order_list.html'
    context_object_name = 'order_lst'
    model = models.OrderModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

# def order_list(request):
#     if request.method == "GET":
#         query = models.OrderModel.objects.all()  # Используем модель OrderModel, а не форму OrderForm
#         context = {'order_lst': query}
#         return render(request, 'order/order_list.html', context)

#добвление
class CreateOrderView(generic.CreateView):
    template_name = 'order/create_order.html'

    def get(self, request):
        form = OrderForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('order_lst')
        return render(request, self.template_name, {'form': form})

# def create_order(request):
#     if request.method == "POST":
#         form = OrderForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('order_lst')
#     else:
#         form = OrderForm()
#
#     return render(request, template_name='order/create_order.html',
#                   context={'form': form})
# удаления
class DeleteOrderView(generic.DetailView):
    def get(self, request, id):
        order = get_object_or_404(models.OrderModel, id=id)
        order.delete()
        return redirect('order_lst')


# def delete_order(request, id):
#     order_id = get_object_or_404(models.OrderModel, id=id)
#     order_id.delete()
#     return redirect('order_lst')


#изменение
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
            return redirect('order_lst')
        return render(request, 'order/update_order.html', {'form': form, 'order_id': order})


# def update_order(request, id):
#     order_id = get_object_or_404(models.OrderModel, id=id)
#     if request.method == "POST":
#         form = forms.OrderForm(request.POST,instance=order_id)
#         if form.is_valid():
#             form.save()
#             return redirect('order_lst')
#     else:
#         form = forms.OrderForm(instance=order_id)
#         return render(request, template_name='order/update_order.html',
#                       context={
#                           'form': form,
#                            'order_id': order_id
#                       })
