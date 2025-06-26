import pandas as pd

print("Lectura CSV")

df = pd.read_csv('data/datos.csv', delimiter=';')
#print(df)
#Primeras 5 filas
print(df.head())
#Podemos agrupar por Ocupacion
df_grupo = df.groupby('ocupacion').size()
print(df_grupo)