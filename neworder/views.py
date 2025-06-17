from django.shortcuts import render, redirect, get_object_or_404
from .models import NewOrder
from .forms import NewOrderForm

def create_order(request):
    if request.method == 'POST':
        form = NewOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = NewOrderForm()
    return render(request, 'neworder_form.html', {'form': form})

def edit_order(request, pk):
    order = get_object_or_404(NewOrder, pk=pk)

    if request.method == 'POST':
        form = NewOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = NewOrderForm(instance=order)

    return render(request, 'neworder_form.html', {'form': form})

