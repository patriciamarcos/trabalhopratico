import pandas as pd

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
        'Máximo': calcular_maximo(valores)
    }

# Exibir as estatísticas descritivas calculadas
for coluna, estatisticas in estatisticas_descritivas.items():
    print(f"Estatísticas para a coluna '{coluna}':")
    for estatistica, valor in estatisticas.items():
        print(f"{estatistica}: {valor}")
    print()