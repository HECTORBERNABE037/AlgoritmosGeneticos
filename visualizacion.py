# src/visualizacion.py

import matplotlib.pyplot as plt

def graficar_convergencia(historial_fitness):
    """
    Muestra un gráfico de cómo el mejor fitness evoluciona a través de las generaciones.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(historial_fitness, marker='o', linestyle='-')
    plt.title('Convergencia del Algoritmo Genético')
    plt.xlabel('Generación')
    plt.ylabel('Mejor Fitness')
    plt.grid(True)
    plt.show()