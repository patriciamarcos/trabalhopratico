import pandas as pd

df1 = pd.read_csv('C:\\Users\\patri\\Desktop\\ubi\\bsc_iacd\\2023_2024\\2_semestre\\elem IA\\trabalho_pratico\\dados\\California_Houses.csv')
df2 = pd.read_csv('C:\\Users\\patri\\Desktop\\ubi\\bsc_iacd\\2023_2024\\2_semestre\\elem IA\\trabalho_pratico\\dados\\California_Housing_CitiesAdded.csv')

print("Estrutura do conjunto de dados 1:")
print(df1.head())
print("\nEstrutura do conjunto de dados 2:")
print(df2.head())

df_combinado = pd.merge(df1, df2, how='outer')

print("\nConjunto de dados combinado:")
print(df_combinado.head())

df_combinado.to_csv('dados_combinado_california.csv', index=False)
