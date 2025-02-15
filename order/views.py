from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from .forms import OrderForm

#добавления
def order_list(request):
    if request.method == "GET":
        query = models.OrderModel.objects.all()  # Используем модель OrderModel, а не форму OrderForm
        context = {'order_lst': query}
        return render(request, 'order/order_list.html', context)

#удаления
def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('order_lst')
    else:
        form = OrderForm()

    return render(request, template_name='order/create_order.html',
                  context={'form': form})
# удаления
def delete_order(request, id):
    order_id = get_object_or_404(models.OrderModel, id=id)
    order_id.delete()
    return redirect('order_lst')


#изменение
def update_order(request, id):
    order_id = get_object_or_404(models.OrderModel, id=id)
    if request.method == "POST":
        form = forms.OrderForm(request.POST,instance=order_id)
        if form.is_valid():
            form.save()
            return redirect('order_lst')
    else:
        form = forms.OrderForm(instance=order_id)
        return render(request, template_name='order/update_order.html',
                      context={
                          'form': form,
                           'order_id': order_id
                      })
