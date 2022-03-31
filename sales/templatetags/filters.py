from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "Kes "+str(number)

@register.filter(name='product')
def product(number , number1):
    return number * number1


@register.filter (name='quantity')
def quantity(order):

    for id in order:
        if int (id) == order.id:
            return order.get (id)
    return 0;


@register.filter (name='sub_total')
def sub_total(order):
    return order.price * quantity (order)


@register.filter (name='grand_total')
def grand_total(orders):
    sum = 0;
    for order in orders:
        sum += sub_total (order)

    return sum
