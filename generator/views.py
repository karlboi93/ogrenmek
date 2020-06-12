from django.shortcuts import render
from django.http import HttpResponse
import random, string

def home(request):
    return render(request, "generator/home.html")

def password(request):
    chars=list(string.ascii_lowercase)
    if request.GET.get("uppercase"):
        chars.extend(list(string.ascii_uppercase))
    if request.GET.get("numbers"):
        chars.extend(string.digits)
    if request.GET.get("special"):
        chars.extend(string.punctuation)
    thepassword = ""
    length = int(request.GET.get("length", 12))
    for i in range(length):
        thepassword += random.choice(chars)
    return render(request, "generator/password.html", {'thepassword': thepassword})
