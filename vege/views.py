# from django.shortcuts import render,redirect
# from.models import *
# # Create your views here.
# def receipes(request):
#   if request.method=="POST":
    
#    data=request.POST
#    Receipe_Image=request.FILES.get('Receipe_Image')
#    ReceipeName=data.get('ReceipeName')
#    Receipe_Descp=data.get('Receipe_Descp')
#   #  print(ReceipeName)
#   #  print( Receipe_Descp)
#   #  print(Receipe_Image)
#   Receipe.objects.create(
#     Receipe_Image=Receipe_Image,
#     ReceipeName =ReceipeName ,
#     Receipe_Descp=Receipe_Descp
#   )
#   return redirect('/receipes/')
#   return render(request,'receipes.html')
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404

from .models import *

def receipes(request):
    if request.method == "POST":
        data = request.POST
        Receipe_Image = request.FILES.get('Receipe_Image')
        ReceipeName = data.get('ReceipeName')
        Receipe_Descp = data.get('Receipe_Descp')

        Receipe.objects.create(
            Receipe_Image=Receipe_Image,
            ReceipeName=ReceipeName,
            Receipe_Descp=Receipe_Descp
        )
        return redirect('/receipes/')  
      

    queryset = Receipe.objects.all()
    return render(request, 'receipes.html', {'receipes': queryset})
  
def delete_recipe(request, id):
  
    receipe = get_object_or_404(Receipe, id=id)
    if request.method == "POST":
        receipe.delete()
    return redirect('/receipes/')
