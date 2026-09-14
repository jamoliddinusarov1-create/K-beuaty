from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    messages.success(request, f'{product.name} savatga qo\'shildi')
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'{product.name} miqdori yangilandi')
    else:
        bag.pop(item_id)
        messages.success(request, f'{product.name} savatdan olib tashlandi')

    request.session['bag'] = bag
    return redirect('view_bag')


def remove_from_bag(request, item_id):
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'{product.name} savatdan olib tashlandi')
        request.session['bag'] = bag
        return redirect('view_bag')
    except Exception as e:
        messages.error(request, f'Xatolik yuz berdi: {e}')
        return redirect('view_bag')