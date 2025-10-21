import numpy as np
import math
import time 
import pandas as pd

#OBS 1: Computar os tempos de treinamento e teste de cada modelo para ajudar a decidir pelo melhor modelo.

#OBS 2: Realizar, no mínimo, 100 rodadas de treinamento-teste independentes dos modelos e obter as 
#estatísticas de desempenho (acurácia média, desvio-padrão, acurácia máxima, acurácia mínima e mediana da 
#acurácia). Determinar a matriz de confusão para a melhor e pior rodada.

#OBS 3: Avaliar o efeito da porcentagem de separação dos dados de treino-teste no desempenho dos 
#classificadores. Sugestão: testar as seguintes possibilidades: 20/80, 30/70, 50/50, 70/30 e 80/20.

#OBS 4: Calcular também as estatísticas de desempenho por classe, com o objetivo de entender se há classes 
#mais fáceis de categorizar que outras
def dividir_dados(dados,rotulos,treino_teste):
    separacao_dos_dados = [[0.20,0.80], [0.30,0.70], [0.50,0.50], [0.70,0.30], [0.80,0.20]]
    quantidade_treino, quantidade_teste = separacao_dos_dados[treino_teste]

    dados = np.array(dados)
    rotulos = np.array(rotulos)

    I = np.random.permutation(len(dados))
    nu_exem_treino = math.floor(quantidade_treino * len(dados))

    Xtrn = dados[I[:nu_exem_treino]]
    Ytrn = rotulos[I[:nu_exem_treino]]
    X_teste = dados[I[nu_exem_treino:]]
    Y_teste = rotulos[I[nu_exem_treino:]]


    return Xtrn,Ytrn,X_teste,Y_teste,I

def Minkowski(x,y,m):
    l=[0.5, 2/3, 1, 3/2, 2, 5/2]#(distância de Minkowski de ordens m ∈ {0,5; 2/3; 1; 3/2; 2; 5/2} 
    m=l[m]
    d=0
    for i in range(len(x)):
        d=d+abs(x[i]-y[i])**m
    d=d**(1/m)
    return d
def ClassificadorKNN(vizinhos,rotulos,testes,rotulos_teste):
    print(vizinhos[0])
    lista_de_testes=[]
    p=0
    acertos=0
    for referencia in testes:
        vizinhos_de_ref=[]
        for vizinho in vizinhos:
            vizinhos_de_ref.append(Minkowski(referencia,vizinho, m=0))


        # Cria pares para manter associação
        pares = list(zip(vizinhos_de_ref, rotulos))

        # Ordena os pares "in place"
        pares.sort(key=lambda x: x[0])  # ordena pelo valor numérico

        # Separa novamente
        vizinhos_de_ref[:], rotulos[:] = zip(*pares)
        if rotulos[0] ==rotulos_teste[p]:
            acertos+=1
        lista_de_testes.append([vizinhos_de_ref,rotulos])
    return  acertos, lista_de_testes
'''
def ClassificadorDMC(vizinhos,rotulos,testes,rotulos_teste): # Classificador Distância Mínima ao Centróide
    
    for i in vizinhos:
           
    
    
    
    return acertos, lista_de_testes
    '''
'''
def ClassificadorDMCvro():
def ClassificadorMC():
'''    
def carregar_dados(nome_arquivo):
    dados=  pd.read_csv(nome_arquivo, sep="\s+", header=None)
    dados
    
    x = (dados.iloc[:, :-1]).to_numpy().tolist()  # Features (todas as colunas menos a última)
    y = (dados.iloc[:, -1]).to_numpy().tolist()  # Rótulos (última coluna)
    return x,y


def analise_acuracias(lista_de_acuracias):
    acuracia_media=np.mean(lista_de_acuracias)
    desvio_padrao_acuracia=np.std(lista_de_acuracias)
    acuracia_maxima=np.max(lista_de_acuracias)
    acuracia_minima=np.min(lista_de_acuracias)
    mediana_acuracia=np.median(lista_de_acuracias)
    return acuracia_media, desvio_padrao_acuracia, acuracia_maxima, acuracia_minima,mediana_acuracia
    

def analise_epoca(dados_epocas):
    melhor_rodada=0
    dados_melhor_rodada=[]
    pior_rodada=10000
    dados_pior_rodada=[]
    acuracias=[]
    for dados in dados_epocas:
        nota_rodada=dados[0]
        dados_rodada=dados[1]
        if melhor_rodada< nota_rodada:
            melhor_rodada=nota_rodada
            dados_melhor_rodada = dados_rodada
        if pior_rodada>nota_rodada:
            pior_rodada=nota_rodada
            dados_pior_rodada = dados_rodada
        acuracia=dados[0]/len(dados)
        acuracias.append(acuracia)
    
    return melhor_rodada, dados_melhor_rodada,pior_rodada,dados_pior_rodada, acuracias
    
def main(): 
    epocas=100
    dados_epocas=[]
    dados, rotulos= carregar_dados("C:/Users/Emanuel/Documents/Detec Padrões/primeiro trabalho/column_3C.dat")
    
    for epoca in range(epocas):
        dados_treino,rotulos_treino,dados_testes,rotulos_testes,I= dividir_dados(dados,rotulos,treino_teste=0)
        acertos, lista_de_testes=ClassificadorKNN(dados_treino,rotulos_treino,dados_testes,rotulos_testes)
        dados_epocas.append([acertos,lista_de_testes])
    melhor_rodada, dados_melhor_rodada,pior_rodada,dados_pior_rodada, acuracias=analise_epoca(dados_epocas)
    acuracia_media, desvio_padrao_acuracia, acuracia_maxima, acuracia_minima,mediana_acuracia=analise_acuracias(acuracias)
    
    print("acuracia media: ",acuracia_media )
    print("desvio_padrao_acuracia: ",desvio_padrao_acuracia)
    print( "acuracia_maxima: ", acuracia_maxima)
    print("acuracia_minima: ",acuracia_minima)
    print("mediana_acuracia: ",mediana_acuracia)
    return


main()