import numpy as np

from data.datos_problema import (
    COSTOS,FERTILIZANTES,REQUERIMIENTOS,TOXICIDAD_MAXIMA,W1_REQUERIMIENTOS,W2_REQUERIMIENTOS,CULTIVOS,LISTA_FERTILIZANTES,NUTRIENTES,NUM_CULTIVOS,NUM_FERTILIZANTES
)

def calcular_fitness(cromosoma):
    #calcula el fitness de un cromosoma minimizando la funcion objetivo
    matriz_solucion = cromosoma.reshape((NUM_CULTIVOS,NUM_FERTILIZANTES))
    #Calculo del costo real
    costo_total=0
    for j, fert_nombre in enumerate(LISTA_FERTILIZANTES):
        cantidad_total_fert = np.sum(matriz_solucion[:,j])
        costo_total += cantidad_total_fert * COSTOS[fert_nombre]

    #calculo de penalizaciones
    for i, cult_nombre in enumerate(CULTIVOS):
        nutrientes_recibidos = {nut: 0 for nut in NUTRIENTES}

        #calculamos el total de nutrientes para el cultivo i
        for j, fert_nombre in enumerate(LISTA_FERTILIZANTES):
            cantidad_aplicada = matriz_solucion[i,j]
            for nut in NUTRIENTES:
                nutrientes_recibidos[nut] += cantidad_aplicada * FERTILIZANTES[fert_nombre][nut]

        #aplicamos la penalizacion para el cultivo
        for nut in NUTRIENTES:
            #penalizacion por deficiencia parte 2 de la ecuacion
            requerimiento_nutriente = REQUERIMIENTOS[cult_nombre][nut]
            if nutrientes_recibidos[nut]< requerimiento_nutriente:
                faltante = requerimiento_nutriente - nutrientes_recibidos[nut]
                penalizacion_total += W1_REQUERIMIENTOS * faltante

            #penalizacion por toxicidad
            toxicicidad_max_nutriente = TOXICIDAD_MAXIMA[nut]
            if nutrientes_recibidos[nut] > toxicicidad_max_nutriente:
                exceso = nutrientes_recibidos[nut] - toxicicidad_max_nutriente
                penalizacion_total +=W2_REQUERIMIENTOS *exceso

    #calculo final
    costo_final_penalizado = costo_total + penalizacion_total

    #convertimos a fitness 
    return -costo_final_penalizado