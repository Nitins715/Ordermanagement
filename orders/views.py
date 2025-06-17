from django.shortcuts import render, get_object_or_404, redirect
from neworder.models import NewOrder
from neworder.forms import NewOrderForm 
from django.utils.dateparse import parse_date

def order_list(request):
    orders = NewOrder.objects.all()
    
    ref = request.GET.get('ref')
    date_str = request.GET.get('date')
    status = request.GET.get('status')

    if ref:
        orders = orders.filter(internal_ref_no__icontains=ref)

    if date_str:
        date = parse_date(date_str)
        if date:
            orders = orders.filter(order_date__date=date)

    if status == 'paid':
        orders = orders.filter(payment_method__isnull=False).exclude(payment_date__isnull=True)
    elif status == 'pending':
        orders = orders.filter(payment_method__isnull=False, payment_date__isnull=True)
    elif status == 'overdue':
        orders = orders.filter(payment_method__isnull=True, payment_date__isnull=True)

    return render(request, 'order_list.html', {'orders': orders})



def create_order(request):
    if request.method == 'POST':
        form = NewOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
        elif():
            pass
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
    return render(request, 'edit_order.html', {'form': form})

def delete_order(request, pk):
    order = get_object_or_404(NewOrder, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'confirm_delete.html', {'order': order})
