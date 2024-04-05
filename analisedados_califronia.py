import pandas as pd
import math

def calcular_media(valores):
    return sum(valores) / len(valores)

# Função para calcular mediana
def calcular_mediana(valores):
    sorted_valores = sorted(valores)
    n = len(sorted_valores)
    if n % 2 == 0:
        return (sorted_valores[n // 2 - 1] + sorted_valores[n // 2]) / 2
    else:
        return sorted_valores[n // 2]

# Função para calcular desvio padrão
def calcular_desvio_padrao(valores):
    media = calcular_media(valores)
    n = len(valores)
    soma_quadrados_diferencas = sum((x - media) ** 2 for x in valores)
    return (soma_quadrados_diferencas / (n - 1)) ** 0.5

# Função para calcular mínimo
def calcular_minimo(valores):
    return min(valores)

# Função para calcular máximo
def calcular_maximo(valores):
    return max(valores)

#Função para calcular a variância
def calcular_variancia(valores):
    total = sum(valores)
    media = total / len(valores)
    diferencas_quadraticas = sum((x - media) ** 2 for x in valores)
    variancia = diferencas_quadraticas / (len(valores) - 1)
    return variancia

#Função para calcular amplitude
def calcular_amplitude(lista):
    amplitude = max(lista) - min(lista)
    return amplitude

#Função para calcular os quadris
def calcular_quartis(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)

    q1_index = (n + 1) // 4
    q2_index = (n + 1) // 2
    q3_index = 3 * (n + 1) // 4

    q1 = lista_ordenada[q1_index - 1] if n % 2 != 0 else (lista_ordenada[q1_index - 1] + lista_ordenada[q1_index]) / 2
    q2 = lista_ordenada[q2_index - 1] if n % 2 != 0 else (lista_ordenada[q2_index - 1] + lista_ordenada[q2_index]) / 2
    q3 = lista_ordenada[q3_index - 1] if n % 2 != 0 else (lista_ordenada[q3_index - 1] + lista_ordenada[q3_index]) / 2

    return {'Q1': q1, 'Q2': q2, 'Q3': q3}


dados_combinados = pd.read_csv('dados_combinado_california.csv')

estatisticas_descritivas = {}

# Loop for para calcular estatísticas descritivas para cada variável
for coluna in dados_combinados.columns:
    valores = dados_combinados[coluna].dropna()  # Remover valores em falta
    estatisticas_descritivas[coluna] = {
        'Média': calcular_media(valores),
        'Mediana': calcular_mediana(valores),
        'Desvio Padrão': calcular_desvio_padrao(valores),
        'Mínimo': calcular_minimo(valores),
        'Máximo': calcular_maximo(valores),
        'Variância': calcular_variancia(valores),
        'Amplitude': calcular_amplitude(valores),
        'Quartis': calcular_quartis(valores)
    }

# Exibir as estatísticas descritivas calculadas
for coluna, estatisticas in estatisticas_descritivas.items():
    print(f"Estatísticas para a coluna '{coluna}':")
    for estatistica, valor in estatisticas.items():
        print(f"{estatistica}: {valor}")
    print()

def covariancia(Median_House_Value, Distance_to_coast):
    media_x = sum(Median_House_Value) / len(Median_House_Value)
    media_y = sum(Distance_to_coast) / len(Distance_to_coast)
    calcular_covariancia = sum((x - media_x)*(y - media_y) for x, y in zip(X, Distance_to_coast))/ (len(X) - 1)
    return calcular_covariancia