import matplotlib.pyplot as plt

#La mayoría de los gráficos tienen un eje X y otro Y
x = ["Betis", "Atletico de Madrid", "Barcelona", "Real Madrid"]
y = [5, 10, 15, 20]

#Mediante plt indicamos el tipo de gráfico que deseamos
plt.bar(x,y)
#Personalizar el gráfico
plt.title("Grafico 26 junio")
plt.xlabel("Equipos")
plt.ylabel("Presupuesto")
plt.savefig('images/equipos.png')
plt.show()