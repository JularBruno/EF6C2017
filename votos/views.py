# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.loader import render_to_string

# Create your views here.
from .models import *


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
    candidatoNulo = Candidato.objects.get(nombre = "Candidato Nulo")
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
 
#-------------------- 
    
    genteDistrito = Distrito.objects.get(cantidad_votantes).count()
    print genteDistrito
    
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

    votos = Votos.objects.all().count()
    votoi= 0
    cantidad_ganador = 0
    ganador = ""
    candidatos = Candidato.objects.all()
    candidatoNulo = Candidato.objects.get(nombre = "Candidato Nulo")

    #genteDistrito = Distrito.objects.filter(cantidad_votantes).count()
    
    
    
    for i in candidatos:
	    if i != candidatoNulo:
		    votoi = Votos.objects.filter(candidato_id = i).count()
		    if votoi == cantidad_ganador:
				ganador += str("Empató con ") + str(i)
				cantidad_ganador = votoi
		    if votoi > cantidad_ganador:
				ganador = i
				cantidad_ganador = votoi
	    
    print ganador
		    
    
    return render(request,'distrital.html',context)
    
    
