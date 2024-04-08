import pandas as pd
from datetime import datetime
from scipy.stats import mstats
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns

dados1 = pd.read_csv('C:\\Users\\patri\\Desktop\\ubi\\bsc_iacd\\2023_2024\\2_semestre\\elem IA\\trabalho_pratico\\dados\\California_Houses.csv')
dados2 = pd.read_csv('C:\\Users\\patri\\Desktop\\ubi\\bsc_iacd\\2023_2024\\2_semestre\\elem IA\\trabalho_pratico\\dados\\Melbourne_housings.csv', low_memory=False)

df1 = dados1.drop(columns={'Median_Income','Population','Households', 'Distance_to_LA', 'Distance_to_SanDiego', 'Distance_to_SanJose', 'Distance_to_SanFrancisco'})
df2 = dados2.drop(columns={'Suburb', 'Type', 'Method', 'Postcode', 'SellerG','Date', 'Car', 'CouncilArea', 'Regionname', 'Propertycount', 'ParkingArea', 'BuildingArea'})

df1 = df1.rename(columns={'Median_House_Value': 'Price', 'Median_Age': 'Age', 'Tot_Rooms': 'Rooms','Tot_Bedrooms': 'Bedroom', 'Distance_to_coast': 'Distance_coast'})
df2 = df2.rename(columns={'YearBuilt': 'Age', 'Longtitude': 'Longitude', 'Distance': 'Distance_coast'})

ano_atual = datetime.now().year
df2['Age'] = ano_atual - df2['Age']

df_combinado = pd.concat([df1, df2], axis=0)

#Preencher valores em falta
colunas_numericas = df_combinado.select_dtypes(include=['number'])
mediana_por_coluna = colunas_numericas.median()
df_combinado[colunas_numericas.columns] = colunas_numericas.fillna(mediana_por_coluna)
print(df_combinado)

#Tratamento outliers
#colunas_para_winsorize = df_combinado.columns.difference(['Address'])

# Aplicar Winsorização Simétrica em todas as colunas selecionadas
#for coluna in colunas_para_winsorize:
#    df_combinado[coluna] = mstats.winsorize(df_combinado[coluna], limits=(0.05, 0.05))

# Verificar o DataFrame resultante
#print(df_combinado)

#Normalização de Dados por Min-Max Scaling
colunas_para_normalizar = df_combinado.columns.difference(['Address'])
scaler = MinMaxScaler()
df_combinado[colunas_para_normalizar] = scaler.fit_transform(df_combinado[colunas_para_normalizar])

colunas_para_plotar = df_combinado.columns.difference(['Address'])
for coluna in colunas_para_plotar:
    plt.hist(df_combinado[coluna])
    plt.xlabel('Valores Normalizados')
    plt.ylabel('Frequência')
    plt.title(f'Distribuição dos Valores Normalizados para a coluna {coluna}')
    plt.show()


####Apresentação narrativa(gráficos)
colunas_para_incluir = df_combinado.columns.difference(['Address'])

# Crie o mapa de calor
plt.figure(figsize=(10, 8))  # Ajuste o tamanho conforme necessário
sns.heatmap(df_combinado[colunas_para_incluir].corr(), annot=True, cmap='coolwarm', fmt=".2f")

# Adicione um título ao mapa de calor
plt.title("Mapa de Calor de Correlação (sem a coluna_a_manter)")

# Exiba o mapa de calor
plt.show()