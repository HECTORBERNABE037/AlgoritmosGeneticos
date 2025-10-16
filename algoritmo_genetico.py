# src/algoritmo_genetico.py

import numpy as np
# --- PIEZA FALTANTE: Importamos la función de fitness ---
from problema import calcular_fitness
from datos_problema import LONGITUD_CROMOSOMA

class AlgoritmoGenetico:
    def __init__(self, tam_poblacion, num_generaciones, tasa_cruce, tasa_mutacion, rango_genes=(0, 20)):
        self.tam_poblacion = tam_poblacion
        self.num_generaciones = num_generaciones
        self.tasa_cruce = tasa_cruce
        self.tasa_mutacion = tasa_mutacion
        self.rango_genes = rango_genes

    def _inicializar_poblacion(self):
        return np.random.uniform(self.rango_genes[0], self.rango_genes[1], size=(self.tam_poblacion, LONGITUD_CROMOSOMA))

    def _seleccionar_padres(self, poblacion, fitness):
        padres = []
        for _ in range(2):
            indices_torneo = np.random.randint(0, len(poblacion), 3)
            participantes_torneo = poblacion[indices_torneo]
            fitness_torneo = fitness[indices_torneo]
            indice_ganador = np.argmax(fitness_torneo)
            padres.append(participantes_torneo[indice_ganador])
        return padres[0], padres[1]

    def _cruzar(self, padre1, padre2):
        punto_cruce = np.random.randint(1, LONGITUD_CROMOSOMA - 1)
        hijo = np.concatenate([padre1[:punto_cruce], padre2[punto_cruce:]])
        return hijo

    def _mutar(self, cromosoma):
        for i in range(LONGITUD_CROMOSOMA):
            if np.random.rand() < self.tasa_mutacion:
                cromosoma[i] = np.random.uniform(self.rango_genes[0], self.rango_genes[1])
        return cromosoma

    # --- PIEZA FALTANTE: El motor del algoritmo ---
    def ejecutar(self):
        # 1. Creamos la primera generación de soluciones al azar
        poblacion = self._inicializar_poblacion()
        historial_fitness = []

        # 2. Empezamos el ciclo evolutivo
        for generacion in range(self.num_generaciones):
            # Calculamos qué tan buena es cada solución en la población actual
            fitness = np.array([calcular_fitness(ind) for ind in poblacion])
            
            # Guardamos el mejor fitness de esta generación para el gráfico
            mejor_fitness_generacion = np.max(fitness)
            historial_fitness.append(mejor_fitness_generacion)
            
            print(f"Generación {generacion + 1}/{self.num_generaciones} - Mejor Fitness: {mejor_fitness_generacion:.2f}")

            # 3. Creamos la siguiente generación
            nueva_poblacion = []
            
            # Elitismo: El mejor individuo de esta generación pasa directamente a la siguiente
            idx_mejor = np.argmax(fitness)
            nueva_poblacion.append(poblacion[idx_mejor])

            # Creamos el resto de la nueva población (tam_poblacion - 1 individuos)
            while len(nueva_poblacion) < self.tam_poblacion:
                padre1, padre2 = self._seleccionar_padres(poblacion, fitness)
                
                if np.random.rand() < self.tasa_cruce:
                    hijo = self._cruzar(padre1, padre2)
                else:
                    hijo = padre1.copy() # Si no hay cruce, uno de los padres pasa
                
                hijo_mutado = self._mutar(hijo)
                nueva_poblacion.append(hijo_mutado)

            # Reemplazamos la vieja población con la nueva y mejorada
            poblacion = np.array(nueva_poblacion)

        # 4. Al final de todas las generaciones, encontramos la mejor solución final
        fitness_final = np.array([calcular_fitness(ind) for ind in poblacion])
        idx_mejor_final = np.argmax(fitness_final)
        
        mejor_solucion = poblacion[idx_mejor_final]
        mejor_fitness = fitness_final[idx_mejor_final]

        # 5. Devolvemos los resultados
        return mejor_solucion, mejor_fitness, historial_fitness