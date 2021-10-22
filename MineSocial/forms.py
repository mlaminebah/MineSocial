from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Mot de passe',widget=forms.PasswordInput)
    
    def clean(self):
        d_propre = super(LoginForm,self).clean ()
        email = d_propre.get("email")
        password = d_propre.get("password")
        if email and password:
            if password != '12' or email != 'la@ici.fr':
                raise forms.ValidationError("Addresse ou mot de passe invalide.")
        return d_propre
            