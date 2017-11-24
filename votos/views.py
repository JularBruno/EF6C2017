# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.
from votos.models import *


def resultado_global(request):
    """
    Generar la vista para devolver el resultado global de la elección.
    Tener en cuenta que tiene que tener:
    Cantidad total de votos por candidato
    Cantidad total de votos nulos
    Porcentaje de cada candidato
    Porcentaje de votos nulos
    Total de votos de la elección
    """
    context={}
    context['distritos'] = Distrito.objects.all()
    
    candidatos = Candidato.objects.all()
    candidatoNulo = Candidato.objects.get(nombre = "Nulo")
    votos = Votos.objects.all().count()
    votoi= 0
    
    for i in candidatos:
	    if i != candidatoNulo:
		    votoi = Votos.objects.filter(candidato_id = i).count()
		    print "voto de " + str(i) + " cantidad: " + str(votoi)
            porcentajeVotos = (votoi * 100)/votos
            print "porc voto " + str(i) + " " + str(porcentajeVotos)
    
    
    votosNull = Votos.objects.filter(candidato_id = candidatos).count()
	
    porcentajeNulos = (votosNull * 100)/votos 	   
	
    print "porce nulos: " + str(porcentajeNulos)
    print "Votos null: " + str(votosNull)
    print "Votos: " + str(votos)
    return render(request,'global.html',context)


def resultado_distrital(request):
    """
    Generar la vista para devolver el resultado distrital de la elección
    Tener en cuenta que tiene que tener:
    Tamaño del padrón
    Porcentaje de votos del distrito (respecto al padron. Ejemplo: Si el distrito tiene 1000 votantes y hay 750 votos, el porcentaje es 75%)
    Total de votos del distrito
    Candidato ganador
    """
    context={}

		    
    
    return render(request,'distrital.html',context)
    
    
