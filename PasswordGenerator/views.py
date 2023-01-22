from django.shortcuts import render
from django.http import HttpResponse
import random
name="Suraj"
age1=23
def age(request):
    return HttpResponse("My name is {} and i am {} old".format(name,age1))
def bird(request):
    return HttpResponse("I love birds")    

def Home(request):
    return render(request,"PasswordGenerator/home.html")  

def about(request):
    return render(request,"PasswordGenerator/about.html")          

def Password(request):
    characters= list("abcdefghijklmnopqrstuvwxyz")
  
    if request.GET.get("Uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("number"):
        characters.extend(list("0123456789"))
    if request.GET.get('Specialcase'):
        characters.extend(list('@#$%&^*+-'))    






    length = int(request.GET.get("length",13))

    

    thepassword=""
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request,"PasswordGenerator/Password.html",{"Password":thepassword})

    
