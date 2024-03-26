#recolha dos dados
import pandas as pd

dados1 = pd.read_csv('C:\\Users\\patri\\Desktop\\ubi\\bsc_iacd\\2023_2024\\2_semestre\\elem IA\\trabalho_pratico\\dados\\California_Houses.csv')
df2 = pd.read_csv('C:\\Users\\patri\\Desktop\\ubi\\bsc_iacd\\2023_2024\\2_semestre\\elem IA\\trabalho_pratico\\dados\\California_Housing_CitiesAdded.csv')

dados2= df2.drop(columns={'ocean_proximity','City'})

print("Dados do ficheiro 1:")
print(dados1.head())
print("\nDados do ficheiro 2:")
print(dados2.head())

#integração dos dados
dados_combinados = pd.merge(dados1, dados2, how='outer')
print("\nConjunto de dados combinado:")
print(dados_combinados.head())

dados_combinados.to_csv('dados_combinado_california.csv', index=False)
