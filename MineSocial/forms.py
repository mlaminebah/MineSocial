from django import forms

from MineSocial.models import Employe, Personne,Etudiant


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

    def clean(self):
        d_propre = super(LoginForm, self).clean()
        email = d_propre.get("email")
        password = d_propre.get("password")
        if email and password:
            resultat = Personne.objects.filter(password=password,email=email)
            if len (resultat) != 1:
                raise forms.ValidationError("Addresse ou mot de passe invalide.")
        return d_propre
    
class StudentProfileForm (forms.ModelForm):
    class Meta:
        model = Etudiant
        exclude =  ('amis',)
class EmployeProfilForm (forms.ModelForm):
    class Meta:
        model = Employe
        exclude = ('amis',)