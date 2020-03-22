import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Fishers IRIS Data Set.csv")

setosa_df = df[df["species"] == "setosa"]
countset = setosa_df["Count"]
sepalwidthset = setosa_df["sepal_width"]
sepallengthset = setosa_df["sepal_length"]
petalwidthset = setosa_df["petal_width"]
petallengthset = setosa_df["petal_length"]

virginica_df = df[df["species"] == "virginica"]
countvir = virginica_df["Count"]
sepalwidthvir = virginica_df["sepal_width"]
sepallengthvir = virginica_df["sepal_length"]
petalwidthvir = virginica_df["petal_width"]
petallengthvir = virginica_df["petal_length"]

versicolor_df = df[df["species"] == "versicolor"]
countver = versicolor_df["Count"]
sepalwidthver = versicolor_df["sepal_width"]
sepallengthver = versicolor_df["sepal_length"]
petalwidthver = versicolor_df["petal_width"]
petallengthver = versicolor_df["petal_length"]

plt.figure(figsize=(12,8))
plt.scatter(countset,sepalwidthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(countvir,sepalwidthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(countver,sepalwidthver, s=12, color=["green"], marker="o", label = "versicolor")

plt.title("IRIS Data Set")
plt.xlabel("Sample")
plt.ylabel("Sepal_Width")
plt.legend()
plt.savefig("Sepal_Width_set_vir_ver")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.scatter(countset,sepallengthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(countvir,sepallengthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(countver,sepallengthver, s=12, color=["green"], marker="o", label = "versicolor")

plt.title("IRIS Data Set")
plt.xlabel("Sample")
plt.ylabel("Sepal_Length")
plt.legend()
plt.savefig("Sepal_Length_set_vir_ver")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.scatter(countset,petalwidthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(countvir,petalwidthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(countver,petalwidthver, s=12, color=["green"], marker="o", label = "versicolor")

plt.title("IRIS Data Set")
plt.xlabel("Sample")
plt.ylabel("Petal_Width")
plt.legend()
plt.savefig("Petal_Width_set_vir_ver")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.scatter(countset,petallengthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(countvir,petallengthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(countver,petallengthver, s=12, color=["green"], marker="o", label = "versicolor")

plt.title("IRIS Data Set")
plt.xlabel("Sample")
plt.ylabel("Petal_Length")
plt.legend()
plt.savefig("Petal_Length_set_vir_ver")
plt.show(block=False)
plt.pause(4)
plt.close("all")