import numpy as np
import math
import time 
import pandas as pd
def teste_ordenar_listas_e_referenciais():
    vizinhos_de_ref=[5,4,3,2,1]
    rotulos=['a','b','d','q','r']
    # Cria pares para manter associação
    pares = list(zip(vizinhos_de_ref, rotulos))
    # Ordena os pares "in place"
    pares.sort(key=lambda x: x[0])  # ordena pelo valor numéric
    # Separa novamente
    vizinhos_de_ref[:], rotulos[:] = zip(*pares)
    
    
    print(vizinhos_de_ref)
    print(rotulos)
    return
teste_ordenar_listas_e_referenciais()