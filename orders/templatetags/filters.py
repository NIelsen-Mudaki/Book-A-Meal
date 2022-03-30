from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "Kes "+str(number)

@register.filter (name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == product.id:
            return True
    return False;


@register.filter (name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == product.id:
            return cart.get (id)
    return 0;


@register.filter (name='sub_total')
def sub_total(product, cart):
    return product.price * cart_quantity (product, cart)


@register.filter (name='grand_total')
def grand_total(products):
    sum = 0;
    for p in products:
        sum += sub_total (p, cart)

    return sum
