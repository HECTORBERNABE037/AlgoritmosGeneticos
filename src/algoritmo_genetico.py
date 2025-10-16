import numpy as np

from data.datos_problema import (LONGITUD_CROMOSOMA)

def _inicializar_poblacion(self):
    return np.random.uniform(self.rango_genes[0],self.rango_genes[1],size=(self.tam_poblacion,LONGITUD_CROMOSOMA))

def _seleccionar_padres(self,poblacion,fitness):
    padres = []
    for _ in range(2):
        #seleccionamos 3 individuos al azar de la poblacion para el torneo
        indices_torneo = np.random.randint(0,len(poblacion),3)
        participantes_torneo = poblacion[indices_torneo]
        fitness_torneo = fitness[indices_torneo]

        #el ganador es el que tien el mayor fitness
        indice_ganador = np.argmax(fitness_torneo)
        padres.append(participantes_torneo[indice_ganador])
    return padres[0], padres[1]

def _cruzar (self, padre1, padre2):
    #elige un punto al azar para cortar el adn (menos los extremos)
    punto_cruce = np.random.randint(1,LONGITUD_CROMOSOMA - 1)
    #el hijoo tiene la primera parte del padre1 y la segunda del padre2
    hijo = np.concatenate([padre1[:punto_cruce],padre2[punto_cruce:]])
    return hijo

def _mutar(self, cromosoma):
    for i in range(LONGITUD_CROMOSOMA):
        if np.random.rand() < self.tasa_mutacion:
            #cambia el valor de este gen por uno nuevo y aleatorio
            cromosoma[i] = np.random.uniform(self.rango_genes[0],self.rango_genes[1])
    return cromosoma

