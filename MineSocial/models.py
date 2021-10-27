# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.base import Model


class Personne(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=70)
    date_naissance = models.DateField()
    email = models.EmailField()
    phone_fixe = models.CharField(max_length=15)
    phone_mobile = models.CharField(max_length=15)
    matricule = models.CharField(max_length=20)
    mot_de_pass = models.CharField(max_length=16)
    amis = models.ManyToManyField('self')
    faculte = models.ForeignKey('Faculte',on_delete=models.CASCADE)
    
    def __str__(self): return self.nom+" "+self.prenom

class Message(models.Model):
    auteur = models.ForeignKey('Personne',on_delete=models.CASCADE)
    contenu = models.TextField()
    date_publication = models.DateField ()
    
    def __str__(self):
        if len (self.contenu) > 20: return self.contenu[:19]+"..."
        else: return self.contenu
    
class Faculte(models.Model):
    nom = models.CharField (max_length=35)
    couleur = models.CharField (max_length=8)
    
    def __str__(self): return self.nom

class Campus(models.Model):
    nom = models.CharField(max_length=70)
    addresse = models.CharField(max_length=80)
    
    def __str__(self): return self.nom
    
class Travail(models.Model):
    titre = models.CharField(max_length=50)
    
    def __str__(self): return self.titre

class Cursus(models.Model):
    titre = models.CharField (max_length=50)
    
    def __str__(self): return self.titre

class Employe(Personne):
    bureau = models.CharField(max_length=35)
    campus = models.ForeignKey('Campus',on_delete=models.CASCADE)
    travail = models.ForeignKey('Travail',on_delete=models.CASCADE)
    

class Etudiant(Personne):
    annee = models.IntegerField ()
    cursus = models.ForeignKey ('Cursus',on_delete=models.CASCADE)