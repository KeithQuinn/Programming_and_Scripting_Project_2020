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

plt.figure(figsize=(20,10))
plt.scatter(countset,sepalwidthset, s=10, color=["red"], marker="*", )
plt.scatter(countvir,sepalwidthvir, s=10, color=["blue"], marker="x")
plt.scatter(countver,sepalwidthver, s=10, color=["green"], marker="o")

plt.title("IRIS Data Set")
plt.xlabel("Sample")
plt.ylabel("Sepal_Width")
plt.savefig("Sepal_Width_set_vir_ver")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(20,10))
plt.scatter(countset,sepallengthset, s=10, color=["red"], marker="*", )
plt.scatter(countvir,sepallengthvir, s=10, color=["blue"], marker="x")
plt.scatter(countver,sepallengthver, s=10, color=["green"], marker="o")

plt.title("IRIS Data Set")
plt.xlabel("Sample")
plt.ylabel("Sepal_Length")
plt.savefig("Sepal_Length_set_vir_ver")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(20,10))
plt.scatter(countset,petalwidthset, s=10, color=["red"], marker="*", )
plt.scatter(countvir,petalwidthvir, s=10, color=["blue"], marker="x")
plt.scatter(countver,petalwidthver, s=10, color=["green"], marker="o")

plt.title("IRIS Data Set")
plt.xlabel("Sample")
plt.ylabel("Petal_Width")
plt.savefig("Petal_Width_set_vir_ver")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(20,10))
plt.scatter(countset,petallengthset, s=10, color=["red"], marker="*", )
plt.scatter(countvir,petallengthvir, s=10, color=["blue"], marker="x")
plt.scatter(countver,petallengthver, s=10, color=["green"], marker="o")

plt.title("IRIS Data Set")
plt.xlabel("Sample")
plt.ylabel("Petal_Length")
plt.savefig("Petal_Length_set_vir_ver")
plt.show(block=False)
plt.pause(4)
plt.close("all")