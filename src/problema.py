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