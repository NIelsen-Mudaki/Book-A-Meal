from django.shortcuts import redirect, render
from .forms import MenuForm
from .models import Menu, MenuDate
from django.http import JsonResponse, response
import datetime
# Create your views here.


def menu(request):
  try:
      current_user = request.COOKIES['users']
  except:
      return redirect("/")
  
  current_date_str = request.COOKIES.get('activedate')
  if request.method == 'POST' and 'menudate' in request.POST:
      menudate = request.POST.get('menudate')
      menudateobj = datetime.datetime.strptime(menudate, '%Y-%m-%d')
      selected_date = menudateobj.date()
      check_date = MenuDate.objects.filter(menu_date=selected_date).first()
      if not check_date:
          new_menu_date = MenuDate(menu_date=selected_date)
          new_menu_date.save()
      response = redirect('menu')
      return response
  print(current_date_str)
  if not current_date_str:
      current_datetime = datetime.datetime.today()
      current_date = current_datetime.date()

      check_date = MenuDate.objects.filter(menu_date=current_date).first()
      if not check_date:
          new_menu_date = MenuDate(menu_date=current_date)
          new_menu_date.save()
      current_date_str = current_date.strftime('%Y-%m-%d')
      # response = redirect('menu')
      # response.set_cookie(key='activedate', value=current_date_str)
      # return response

  menudateobj = datetime.datetime.strptime(current_date_str, '%Y-%m-%d')
  active_date = menudateobj.date()
  active_menu_date = MenuDate.objects.filter(menu_date=active_date).first()
  try:
      active_menu_items = active_menu_date.menus.all()
      active_menu_ids = list(menu.id for menu in active_menu_items)
      inactive_menu_items = Menu.get_menu_list_to_assign(active_menu_ids)
  except:
      active_menu_items = []
      inactive_menu_items = []

  context = {
      'activemenuitems': active_menu_items,
      'inactivemenuitems': inactive_menu_items,
      'menudate': current_date_str,
  }
  return render(request, 'admin-menu/admin-menu.html', context)


def create_menu(request):
    meal = request.POST.get('meal')
    print(meal)
    target_date = request.COOKIES.get('activedate')
    target_date_object = datetime.datetime.strptime(target_date, '%Y-%m-%d')

    print(target_date_object)
    if request.method == 'POST':
        meal = request.POST.get('meal')
        additional_items = request.POST.get('additional')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES['mealimage']
        parent_menu_date = MenuDate.objects.filter(
            menu_date=target_date_object.date()).first()

        print(description)

        new_menu = Menu(meal=meal, price=price,
                        description=description, image=image)

        new_menu.save()
        new_menu.menu_date.add(parent_menu_date)
        return redirect('menu')


def edit_menu(request, id):
    if request.method == 'POST':
        target_menu = Menu.objects.filter(id=id).first()
        if target_menu:
            meal = request.POST.get('meal')
            additional_items = request.POST.get('additional')
            price = request.POST.get('price')
            description = request.POST.get('description')
            try:
                image = request.FILES['mealimage']
            except:
                image = None

            if image:
                target_menu.edit_menu(
                    meal=meal, price=price, description=description, image=image)
            else:
                target_menu.edit_menu(
                    meal=meal, price=price, description=description)

            return redirect('menu')

    target_menu = Menu.objects.filter(id=id).first()

    context = {
        "menu": target_menu
    }

    if target_menu == None:
        return redirect('menu')
    return render(request, 'admin-menu/edit-menu.html', context)


def available(request, id):
    print('available')
    target_menu = Menu.objects.filter(id=id).first()
    target_date = request.COOKIES.get('activedate')
    target_date_object = datetime.datetime.strptime(target_date, '%Y-%m-%d')
    target_menu_date = MenuDate.objects.filter(
        menu_date=target_date_object.date()).first()
    target_menu.menu_date.add(target_menu_date)

    return redirect('menu')


def make_unavailable(request, id):
    target_menu = Menu.objects.filter(id=id).first()
    target_date = request.COOKIES.get('activedate')
    target_date_object = datetime.datetime.strptime(target_date, '%Y-%m-%d')
    target_menu_date = MenuDate.objects.filter(
        menu_date=target_date_object.date()).first()
    target_menu_date.menus.remove(target_menu)
    return redirect('menu')


def delete_menu(request, id):
    target_menu = Menu.objects.filter(id=id).first()
    target_menu.delete_menu()
    return redirect('menu')
