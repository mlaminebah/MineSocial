# -*- coding: utf-8 -*-

from django.http import HttpResponse

def welcome (request):
    reponse = """<!DOCTYPE html>
                    <html>
                        <head>
                            <meta charset="utf-8">
                            <title>MineSocial</title>
                         </head>
                         <body>
                             <p>Bienvenue sur mon MineSocial</p>
                        </body>
                    </html>"""
    
    return HttpResponse(reponse)