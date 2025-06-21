from django.shortcuts import render, get_object_or_404, redirect
from neworder.models import NewOrder
from neworder.forms import NewOrderForm 
from django.utils.dateparse import parse_date


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

import openpyxl
from django.http import HttpResponse

def export_to_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Data"

    ws.append(['Order ID' ,'Order Date' ,'Type','Name', 'Contact', 'Skip Size', 'Qty', 'Amount', 'Payment'])

    for obj in NewOrder.objects.all():
        ws.append([obj.internal_ref_no,obj.order_date.date().strftime('%d-%m-%Y'),obj.order_type,obj.name_or_company,obj.contact_number,obj.skip_size,obj.quantity,obj.total_amount_with_vat,obj.payment_method])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=data.xlsx'
    wb.save(response)

    return response


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('order_list')  # replace with your home page name
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def order_list(request):
    orders = NewOrder.objects.all()

    ref = request.GET.get('ref')
    from_date_str = request.GET.get('from_date')
    to_date_str = request.GET.get('to_date')
    status = request.GET.get('status')

    if ref:
        orders = orders.filter(internal_ref_no__icontains=ref)

    from_date = parse_date(from_date_str) if from_date_str else None
    to_date = parse_date(to_date_str) if to_date_str else None

    if from_date:
        orders = orders.filter(order_date__date__gte=from_date)
    if to_date:
        orders = orders.filter(order_date__date__lte=to_date)

    if status == 'paid':
        orders = orders.filter(payment_method__isnull=False, payment_date__isnull=False)
    elif status == 'pending':
        orders = orders.exclude(payment_method__isnull=False, payment_date__isnull=False)

    return render(request, 'order_list.html', {'orders': orders})

@login_required
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

@login_required
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

@login_required
def delete_order(request, pk):
    order = get_object_or_404(NewOrder, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'confirm_delete.html', {'order': order})

