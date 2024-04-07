import pandas as pd
###Reclha de Dados
#carregar os dados dois arquivos CSV
dados1 = pd.read_csv('C:\\Users\\patri\\Desktop\\ubi\\bsc_iacd\\2023_2024\\2_semestre\\elem IA\\trabalho_pratico\\dados\\melbourne_housing.csv')
dados2 = pd.read_csv('C:\\Users\\patri\\Desktop\\ubi\\bsc_iacd\\2023_2024\\2_semestre\\elem IA\\trabalho_pratico\\dados\\Melbourne_housings.csv', low_memory=False)

df1 = dados1.drop(columns={'Rooms','SellerG','Date','Propertycount','Suburb','Address','Type', 'Method', 'CouncilArea', 'Regionname'})
df2 = dados2.drop(columns={'Rooms','SellerG','Date','Propertycount','ParkingArea','Suburb','Address','Type', 'Method', 'CouncilArea', 'Regionname'})


#Exibie as rimeiras linhas para garantir que os dados foram carregados
print("Dados do ficheiro 1:")
print(df1.head())
print("\nDados do ficheiro 2:")
print(df2.head())

###Integração de Dados
df_combinado = pd.concat([df1, df2], axis=0)

print("\nConjunto de dados combinado:")
print(df_combinado.head())

df_combinado.to_csv('dados_combinado_melbourne.csv', index=False)





