from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import OrderForm
from orders.models import Order


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Savatingiz bo'sh")
        return redirect('products')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            from bag.contexts import bag_contents
            current_bag = bag_contents(request)
            total = current_bag['total']

            order = form.save(commit=False)
            order.amount = total
            order.save()

            request.session['bag'] = {}  # savatni tozalash

            return redirect('checkout_success', order_number=order.id)
        else:
            messages.error(request, "Iltimos, formani to'g'ri to'ldiring")
    else:
        form = OrderForm()

    from bag.contexts import bag_contents
    current_bag = bag_contents(request)

    context = {
        'form': form,
        'total': current_bag['total'],
    }
    return render(request, 'checkout/checkout.html', context)


def checkout_success(request, order_number):
    # Agar buyurtma topilmasa, crash bo'lmasdan foydalanuvchiga chiroyli 404 sahifasini ko'rsatadi
    order = get_object_or_404(Order, id=order_number)
    context = {
        'order': order,
    }
    return render(request, 'checkout/checkout_success.html', context)