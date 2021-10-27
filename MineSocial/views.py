# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime
from MineSocial.forms import LoginForm
from MineSocial.forms import StudentProfileForm,EmployeProfilForm

def welcome(request):
    return render(request, "welcome.html", {"current_date_time": datetime.now})


"""def login (request):
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
        return render (request,'login.html')"""


def login(request):
    # vérification que le formulaire ai été envoyé
    if len(request.POST) > 0:
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect("/welcome")
        else:
            return render(request, "login.html", {"form": form})
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})

def register (request):
    if len(request.GET) > 0 and 'profileType' in request.GET:
        studentForm = StudentProfileForm(prefix="st")
        employeForm = EmployeProfilForm(prefix="em")
        
        if request.GET['profileType'] == 'student':
            studentForm = StudentProfileForm(request.GET,prefix="st")
            if studentForm.is_valid ():
                studentForm.save ()
                return redirect ('/login')
        elif request.GET['profileType'] == 'employe':
            employeForm = EmployeProfilForm (request.GET,prefix="em")
            if employeForm.is_valid ():
                employeForm.save ()
                return redirect ('/login')
        return render (request,'user_profile.html',{'studentForm':studentForm,'employeForm':employeForm})
    else:
        studentForm = StudentProfileForm (prefix="st")
        employeForm = EmployeProfilForm (prefix="em")
        return render (request,'user_profile.html',{'studentForm':studentForm,'employeForm':employeForm})