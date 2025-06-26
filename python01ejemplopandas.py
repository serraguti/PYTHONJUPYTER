import pandas as pd

print("Ejemplo de DataFrame")
#Creamos un diccionario con lo que se denominan SERIES de DATOS
#para almacenar en un DataFrame
datos = {
    "nombres": ['Lucia', 'Antonia', 'Adrian', 'Alex'],
    "edad": [22, 46, 27, 55],
    "ciudad": ["Gijon", "Toledo", "Madrid", "Alicante"]
}
#Almacenamos los datos en un DataFrame
df = pd.DataFrame(datos)
print(df)
#PODEMOS PERFECTAMENTE FILTRAR LOS DATOS QUE ESTAMOS VIENDO
#df [ df[COLUMNA] == valor]
print("-----------DataFrame filtrado-----------")
df_filtrado = df[df['edad'] > 30]
print(df_filtrado)

print("-----------DataFrame ordenado----------------")
df_sorted = df.sort_values('edad')
print(df_sorted)