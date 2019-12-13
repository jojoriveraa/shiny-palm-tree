
import pandas as pd
import matplotlib.pyplot as plt

population = pd.read_csv("poblacion.csv")
print(population)

stat = pd.DataFrame()
stat["mean"] = population.groupby("Code")["Total"].mean()
print(stat)

stat["devstd"] = population.groupby("Code")["Total"].std()
print(stat)
