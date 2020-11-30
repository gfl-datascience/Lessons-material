import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("iris_dataset.csv")

setosa_sepal_len = list(df[df['class'].isin(['Iris-setosa'])]["sepal_len"])
setosa_sepal_width = list(df[df['class'].isin(['Iris-setosa'])]["sepal_width"])
versicolor_sepal_len = list(df[df['class'].isin(['Iris-versicolor'])]["sepal_len"])
versicolor_sepal_width = list(df[df['class'].isin(['Iris-versicolor'])]["sepal_width"])
virginica_sepal_len = list(df[df['class'].isin(['Iris-virginica'])]["sepal_len"])
virginica_sepal_width = list(df[df['class'].isin(['Iris-virginica'])]["sepal_width"])

plt.plot(setosa_sepal_len,setosa_sepal_width,"ro")
plt.plot(versicolor_sepal_len,versicolor_sepal_width,"bo")
plt.plot(virginica_sepal_len,virginica_sepal_width,"go")
plt.show()

setosa_petal_len = list(df[df['class'].isin(['Iris-setosa'])]["petal_len"])
setosa_petal_width = list(df[df['class'].isin(['Iris-setosa'])]["petal_width"])
versicolor_petal_len = list(df[df['class'].isin(['Iris-versicolor'])]["petal_len"])
versicolor_petal_width = list(df[df['class'].isin(['Iris-versicolor'])]["petal_width"])
virginica_petal_len = list(df[df['class'].isin(['Iris-virginica'])]["petal_len"])
virginica_petal_width = list(df[df['class'].isin(['Iris-virginica'])]["petal_width"])

plt.plot(setosa_petal_len,setosa_petal_width,"ro")
plt.plot(versicolor_petal_len,versicolor_petal_width,"bo")
plt.plot(virginica_petal_len,virginica_petal_width,"go")
plt.show()