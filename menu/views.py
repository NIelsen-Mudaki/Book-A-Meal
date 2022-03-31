from django.shortcuts import redirect, render
from .forms import MenuForm
from .models import Menu
from django.http import JsonResponse
# Create your views here.

def menu(request):
  
  active_menu_items=Menu.get_active_menu_items()
  inactive_menu_items=Menu.get_inactive_menu_items()

  form=MenuForm()
  context={
    'form':form,
    'activemenuitems':active_menu_items,
    'inactivemenuitems':inactive_menu_items
  }
  return render(request,'admin-menu/admin-menu.html',context)

def create_menu(request):
  meal=request.POST.get('meal')
  print(meal)
  if request.method=='POST':
    meal=request.POST.get('meal')
    additional_items=request.POST.get('additional')
    price=request.POST.get('price')
    description=request.POST.get('description')
    image=request.FILES['mealimage']
    print(description)

    new_menu=Menu(meal=meal,price=price,description=description,image=image)
    print(request.FILES["mealimage"])
    print(image)
    print('jus done')
    new_menu.save()
    # data={'success':'You have been successfully rated this project'}
    # return JsonResponse(data)
    return redirect('menu')


def edit_menu(request,id):
  if request.method=='POST':
      target_menu=Menu.objects.filter(id=id).first()
      if target_menu:
        meal=request.POST.get('meal')
        additional_items=request.POST.get('additional')
        price=request.POST.get('price')
        description=request.POST.get('description')
        try:
          image=request.FILES['mealimage']
        except:
          image=None
        
        
        if image:
          target_menu.edit_menu(meal=meal,price=price,description=description,image=image)
        else:
          target_menu.edit_menu(meal=meal,price=price,description=description)
          
        
        
        
        
        
        # data={'success':'You have been successfully rated this project'}
        # return JsonResponse(data)
        return redirect('menu')
      
  
  target_menu=Menu.objects.filter(id=id).first()

  context={
      "menu":target_menu
    }
  
  if target_menu==None:
    return redirect('menu')
  return render(request,'admin-menu/edit-menu.html',context)


def available(request,id):
  target_menu=Menu.objects.filter(id=id).first()
  target_menu.change_status()

  return redirect('menu')

def make_unavailable(request):
  pass

def delete_menu(request,id):
  target_menu=Menu.objects.filter(id=id).first()
  target_menu.delete_menu()
  return redirect('menu')

