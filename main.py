# src/main.py

from algoritmo_genetico import AlgoritmoGenetico
from visualizacion import graficar_convergencia
from datos_problema import NUM_CULTIVOS, NUM_FERTILIZANTES, CULTIVOS, LISTA_FERTILIZANTES



# --- PARÁMETROS DEL EXPERIMENTO (¡Puedes jugar con estos valores!) ---
TAM_POBLACION = 100
NUM_GENERACIONES = 10000
TASA_CRUCE = 0.9
TASA_MUTACION = 0.15

def main():
    print("Iniciando optimización con Algoritmo Genético...")
    
    # 1. Creamos una instancia de nuestro algoritmo con los parámetros definidos
    ag = AlgoritmoGenetico(
        tam_poblacion=TAM_POBLACION,
        num_generaciones=NUM_GENERACIONES,
        tasa_cruce=TASA_CRUCE,
        tasa_mutacion=TASA_MUTACION
    )
    
    # 2. Ejecutamos el algoritmo y obtenemos los resultados
    mejor_solucion, mejor_fitness, historial = ag.ejecutar()
    
    # 3. Mostramos los resultados de forma clara en la consola
    print("\n--- ¡Optimización Finalizada! ---")
    print(f"Mejor Fitness encontrado: {mejor_fitness:.4f}")
    print(f"Costo total (valor positivo del fitness): {-mejor_fitness:.2f}")
    
    print("\nMejor combinación de fertilizantes (en kg):")
    solucion_matriz = mejor_solucion.reshape((NUM_CULTIVOS, NUM_FERTILIZANTES))
    
    header = "Cultivo | " + " | ".join(f"{f:<6}" for f in LISTA_FERTILIZANTES)
    print(header)
    print("-" * len(header))
    for i, cultivo_nombre in enumerate(CULTIVOS):
        cantidades = " | ".join([f"{kg:6.2f}" for kg in solucion_matriz[i, :]])
        print(f"{cultivo_nombre:^7} | {cantidades}")
        
    # 4. Mostramos el gráfico de convergencia
    graficar_convergencia(historial)


# Este es el punto de entrada que ejecuta todo cuando corres el archivo
if __name__ == "__main__":
    main()