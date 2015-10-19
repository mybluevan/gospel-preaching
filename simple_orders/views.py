from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from simple_orders.models import Order, Product, OrderItem
from simple_orders.forms import OrderForm, OrderItemFormSet
from django.template import RequestContext
from django.core.paginator import Paginator
from django.conf import settings
from django.core.urlresolvers import reverse

def product_list(request):
    page = request.GET.get('page', 1)
    try:
        perpage = settings.PRODUCTS_PER_PAGE
    except AttributeError:
        perpage = 10
    pager = Paginator(Product.objects.all(), perpage)
    return render_to_response('simple_orders/product_index.html', {'products': pager.page(page).object_list, 'page': pager.page(page), 'pager': pager}, context_instance = RequestContext(request))

def product_detail(request, slug):
    p = get_object_or_404(Product, slug__exact=slug)
    cart = request.session.get('cart', list())
    cart_item = None
    for i in cart:
        if i.product.pk == p.pk:
            cart_item = i
    return render_to_response('simple_orders/product_detail.html', {'product': p, 'cart_item': cart_item}, context_instance = RequestContext(request))

def order_confirm(request):
    order = request.session.get('order', None)
    return render_to_response('simple_orders/order_confirm.html', {'order': order}, context_instance = RequestContext(request))

def cart_checkout(request):
    order = Order()
    if request.method == 'POST':
        cart = request.session.get('cart', list())
        if len(cart) == 0:
            return HttpResponseRedirect(reverse(checkout))
        form = OrderForm(request.POST)
        order_items = request.session['cart']
        shipping_cost = order.calc_ship_cost(request.session['cart'])
        sub_total = order.calc_sub_total(cart)
        total = order.calc_total(request.session['cart'])
        if form.is_valid():
            if request.user.is_authenticated():
                order = form.save(commit=False)
                order.user = request.user
                order.save()
            else:
                order = form.save()
            for order_item in request.session['cart']:
                order_item.order = order
                order_item.save()
            request.session['cart'] = list()
            request.session['order'] = order
            return HttpResponseRedirect(reverse(order_confirm))
    else:
        cart = request.session.get('cart', list())
        form = OrderForm()
        order_items = cart
        shipping_cost = order.calc_ship_cost(cart)
        sub_total = order.calc_sub_total(cart)
        total = order.calc_total(cart)
    return render_to_response('simple_orders/checkout.html', {'order_form': form, 'order_items': order_items, 'shipping_cost': shipping_cost, 'total': total, 'sub_total': sub_total}, context_instance = RequestContext(request))

def product_add_to_cart(request, slug):
    quantity = request.POST.get('quantity', 1)
    p = get_object_or_404(Product, slug__exact=slug)
    cart = request.session.get('cart', list())
    if p.qoh >= int(quantity):
        cart.append(OrderItem(product=p, quantity=int(quantity)))
    request.session['cart'] = cart
    return HttpResponseRedirect(p.get_absolute_url())

def cart_detail(request):
    order = Order()
    if request.method == 'POST':
        cart = request.session.get('cart', list())
        if len(cart) == 0:
            return HttpResponseRedirect(reverse(update_cart))
        sub_total = order.calc_sub_total(cart)
        shipping_cost = order.calc_ship_cost(cart)
        total = order.calc_total(cart)
        formset = OrderItemFormSet(data=request.POST, init_instances=cart)
        if formset.is_valid():
            cart = list()
            for form in formset.forms:
                try:                
                    if not form.cleaned_data['DELETE']:
                        order_item = form.instance
                        order_item.quantity = form.cleaned_data['quantity']
                        if order_item.quantity > 0:
                            cart.append(order_item)
                except AttributeError:
                    pass
            request.session['cart'] = cart
            return HttpResponseRedirect(reverse(update_cart))
    else:
        cart = request.session.get('cart', list())
        sub_total = order.calc_sub_total(cart)
        shipping_cost = order.calc_ship_cost(cart)
        total = order.calc_total(cart)
        formset = OrderItemFormSet(init_instances=cart)
    return render_to_response('simple_orders/cart.html', {'shipping_cost': shipping_cost, 'total': total, 'cart_formset': formset, 'sub_total': sub_total}, context_instance = RequestContext(request))
