import pandas as pd
import matplotlib.pyplot as plt

population = pd.read_csv("poblacion.csv")
print(population)

stats = pd.DataFrame()
stats["avg"] = population.groupby("Code")["Total"].mean()
print(stats)

stats["devstd"] = population.groupby("Code")["Total"].std()
print(stats)

stats = stats.sort_values(by = "avg", ascending = False)
print(stats)

topAvgs = pd.DataFrame()
topAvgs = stats[stats["avg"] > 200000000]
print(topAvgs)

x = range(0, len(topAvgs.index))
print(x)

plt.plot(topAvgs.index, topAvgs["avg"], color = "green", marker = "o", label = "Promedio de la poblacion")
plt.plot(topAvgs.index, topAvgs["devstd"], color = "blue", marker = "+", label = "Desviacion estandar")

plt.legend()
plt.xticks(rotation = 90)
plt.xlabel("Pais")
plt.ylabel("Poblacion")
plt.grid(True)
plt.title("Analisis de la poblacion mundial")
plt.show()
