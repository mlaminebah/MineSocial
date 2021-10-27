# Generated by Django 3.2.7 on 2021-10-23 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=70)),
                ('addresse', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Cursus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Faculte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=35)),
                ('couleur', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=70)),
                ('date_naissance', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_fixe', models.CharField(max_length=15)),
                ('phone_mobile', models.CharField(max_length=15)),
                ('matricule', models.CharField(max_length=20)),
                ('mot_de_pass', models.CharField(max_length=16)),
                ('amis', models.ManyToManyField(related_name='_MineSocial_personne_amis_+', to='MineSocial.Personne')),
                ('faculte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MineSocial.faculte')),
            ],
        ),
        migrations.CreateModel(
            name='Travail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date_publication', models.DateField()),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MineSocial.personne')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MineSocial.personne')),
                ('annee', models.IntegerField()),
                ('cursus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MineSocial.cursus')),
            ],
            bases=('MineSocial.personne',),
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MineSocial.personne')),
                ('bureau', models.CharField(max_length=35)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MineSocial.campus')),
                ('travail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MineSocial.travail')),
            ],
            bases=('MineSocial.personne',),
        ),
    ]
