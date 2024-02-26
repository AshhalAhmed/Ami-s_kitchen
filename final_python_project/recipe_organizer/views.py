from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# Create your views here.
def recipes(request):
    if request.method=="POST":
        data=request.POST
        recipe_name=data.get("recipe_name")
        recipe_text=data.get("recipe_text")
        recipe_picture=request.FILES.get("recipe_picture")
        
        recipe.objects.create(
            recipe_name=recipe_name,
            recipe_picture=recipe_picture,
            recipe_text= recipe_text

            )

    datalist=recipe.objects.all()
    if request.GET.get('searchs'):
        datalist=datalist.filter(recipe_name__icontains = request.GET.get('searchs'))
    get_data={'recipes':datalist}
    return render(request,'recipes.html',get_data)

def delete_recipe(request, id):
    recipe_instance = recipe.objects.get(id=id)
    recipe_instance.delete()
    return redirect('recipes')
def update_recipe(request, id):
    recipe_instance = get_object_or_404(recipe, id=id)

    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_text = data.get("recipe_text")
        recipe_picture = request.FILES.get("recipe_picture")
        
        recipe_instance.recipe_name = recipe_name
        recipe_instance.recipe_text = recipe_text

        if recipe_picture:
            recipe_instance.recipe_picture = recipe_picture

        recipe_instance.save()
        return redirect('recipes')
        
    get_data = {'recipe': recipe_instance} 
    return render(request, 'update.html', get_data)
    