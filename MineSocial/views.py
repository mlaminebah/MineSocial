# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime

def welcome (request):
    return render (request,'welcome.html',{'current_date_time': datetime.now})
def login (request):
    #verfie si le formulaire à été envoyé : il faut que la taille du tableau post soit différent de 0
    if len(request.POST) > 0:
        #on véririe si les paramètres attends sont transmis
        if 'email' not in request.POST or 'password' not in request.POST:
            error = "vous devez renseigner l'email et le mot de passe"
            #return render (request,'login.html',{'error':error})
        else:
            email,paswd = request.POST['email'],request.POST['password']
            #vérification des identifiants
            if email != 'lamine@ici.fr' or paswd != 'lamine':
                #si not ok
                error = "Email ou mot de passe Invalide"
                #return render (request,'login.html',{'error':error})
            else:
                #si ok -> page d'accueil
                return redirect ('/welcome')
        return render (request,'login.html',{'error':error})
    else:
        return render (request,'login.html')