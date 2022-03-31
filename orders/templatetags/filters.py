from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "Kes "+str(number)

@register.filter(name='product')
def product(number , number1):
    return number * number1

@register.filter (name='grand_total')
def grand_total(orders):
    sum = 0;
    for order in orders:
        sum += product (order)

    return sum
