COSTOS = {#costo por kg de cada fertilizante
    'F1':10,
    'F2':12,
    'F3':8,
    'F4':15
}
FERTILIZANTES = {#Composicion de nutrientes (ppm por kg) de cada fertilizante
    'F1':{'N':10,'P':10,'K':0,'Micro':2},
    'F2':{'N':0,'P':15,'K':5,'Micro':1},
    'F3':{'N':5,'P':0,'K':10,'Micro':0},
    'F4':{'N':2,'P':2,'K':2,'Micro':5}
}
REQUERIMIENTOS = {#Requirimiento de nutrientes (ppm totales) por cultivo
    'C1':{'N':100,'P':50,'K':0,'Micro':10},
    'C2':{'N':80,'P':80,'K':50,'Micro':8},
    'C3':{'N':90,'P':40,'K':60,'Micro':12}
}
TOXICIDAD_MAXIMA = {#Restricciones de toxicidad (maximas ppm por cultivo)
    'N':120,
    'P':70,
    'K':70,
    'Micro':15
}
#cantidad de penalizacion para la primera parte de la funcion objetivo
W1_REQUERIMIENTOS = 10.0
W2_TOXICIDAD = 20.0
#parametros para el problema
CULTIVOS = list(REQUERIMIENTOS.keys())
LISTA_FERTILIZANTES = list(COSTOS.keys())
NUTRIENTES = list(TOXICIDAD_MAXIMA.keys())

NUM_CULTIVOS = len(CULTIVOS)
NUM_FERTILIZANTES = len(LISTA_FERTILIZANTES)

LONGITUD_CROMOSOMA = NUM_CULTIVOS *NUM_FERTILIZANTES