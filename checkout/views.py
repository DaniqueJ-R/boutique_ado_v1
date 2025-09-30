from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There are no items in your bag.')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51SD9GfBmYOT5xLk0Ykr5gAbnu8PcxOCxXNn7dwh2ZRR61brPPDJ4kVOrbkX0JbKqCUkXfI1FSZCMt0fM0K9eJU8r00316FuTcu',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
