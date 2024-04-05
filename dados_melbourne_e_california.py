import pandas as pd
###Reclha de Dados
#carregar os dados dois arquivos CSV
dados1 = pd.read_csv('C:\\Users\\carlo\\OneDrive\\Documentos\\GitHub\\trabalhopratico\\dados_combinado_california.csv')
dados2 = pd.read_csv('C:\\Users\\carlo\\OneDrive\\Documentos\\GitHub\\trabalhopratico\\dados_combinado_melbourne.csv')

print("Dados do ficheiro 1:")
print(dados1.head())
print("\nDados do ficheiro 2:")
print(dados2.head())

###Integração de Dados
df_combinado = pd.concat([dados1, dados2], axis=0)

print("\nConjunto de dados combinado:")
print(df_combinado.head())

df_combinado.to_csv('dados_combinado_melbourne.csv', index=False)

