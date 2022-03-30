from django.shortcuts import redirect, render
from .forms import MenuForm
from .models import Menu
from django.http import JsonResponse
# Create your views here.

def menu(request):
  
  if request.method=='POST':
    pass

  form=MenuForm()
  context={
    'form':form
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