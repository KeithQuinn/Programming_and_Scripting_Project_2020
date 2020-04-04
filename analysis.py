import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv("Fishers IRIS Data Set.csv")

sepalwidth = df["sepal_width"]
sepallength = df["sepal_length"]
petalwidth = df["petal_width"]
petallength = df["petal_length"]
species = df["species"] 

print("IRIS Data Set:")
print(df.loc[:, df.columns != 'Count'])
print("")
print("The number of each species is: ")
print(df["species"].value_counts())
print("")

shapiro_test_sepal_width = (stats.shapiro(sepalwidth))
shapiro_test_sepal_length = (stats.shapiro(sepallength))
shapiro_test_petal_width = (stats.shapiro(petalwidth))
shapiro_test_petal_length = (stats.shapiro(petallength))

if (shapiro_test_sepal_width[1]) >= 0.05:
    print("Sepal Width is Normally Distributed")
else:
    print("Sepal Width is not Normally Distributed")

if (shapiro_test_sepal_length[1]) >= 0.05:
    print("Sepal Lenght is Normally Distributed")
else:
    print("Sepal Lenght is not Normally Distributed")

if (shapiro_test_petal_width[1]) >= 0.05:
    print("Petal Width is Normally Distributed")
else:
    print("Petal Width is not Normally Distributed")

if (shapiro_test_petal_length[1]) >= 0.05:
    print("Petal Length is Normally Distributed")
else:
    print("Petal Length is not Normally Distributed")

plt.figure(figsize=(12,8))
plt.hist(sepalwidth, bins = 20, rwidth = 0.9)
plt.title("Sepal_Width")
plt.xlabel("Measurment in cm")
plt.ylabel("Observations")
plt.savefig("Sepal_Width_Hist")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.hist(sepallength, bins = 20, rwidth = 0.9)
plt.title("Sepal_Length")
plt.xlabel("Measurment in cm")
plt.ylabel("Observations")
plt.savefig("Sepal_Length_Hist")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.hist(petalwidth, bins = 20, rwidth = 0.9)
plt.title("Petal_Width")
plt.xlabel("Measurment in cm")
plt.ylabel("Observations")
plt.savefig("Petal_Width_Hist")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.hist(petallength, bins = 20, rwidth = 0.9)
plt.title("Petal_Length")
plt.xlabel("Measurment in cm")
plt.ylabel("Observations")
plt.savefig("Petal_Length_Hist")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
sns.set(style="whitegrid")
ax = sns.boxplot(x=species, y = sepalwidth)
plt.title("sepal_width_boxplot")
plt.savefig("sepal_width_boxplot")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
ax = sns.boxplot(x=species, y = sepallength)
plt.title("sepal_length_boxplot")
plt.savefig("sepal_length_boxplot")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
ax = sns.boxplot(x=species, y = petalwidth)
plt.title("petal_width_boxplot")
plt.savefig("petal_width_boxplot")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
ax = sns.boxplot(x=species, y = petallength)
plt.title("petal_length_boxplot")
plt.savefig("petal_length_boxplot")
plt.show(block=False)
plt.pause(4)
plt.close("all")

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
plt.title("sepal_width_scatter")
plt.xlabel("")
plt.ylabel("Sepal_Width")
plt.legend()
plt.savefig("sepal_width_scatter")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.scatter(countset,sepallengthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(countvir,sepallengthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(countver,sepallengthver, s=12, color=["green"], marker="o", label = "versicolor")
plt.title("sepal_length_scatter")
plt.xlabel("")
plt.ylabel("Sepal_Length")
plt.legend()
plt.savefig("sepal_length_scatter")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.scatter(countset,petalwidthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(countvir,petalwidthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(countver,petalwidthver, s=12, color=["green"], marker="o", label = "versicolor")
plt.title("petal_width_scatter")
plt.xlabel("")
plt.ylabel("Petal_Width")
plt.legend()
plt.savefig("petal_width_scatter")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.scatter(countset,petallengthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(countvir,petallengthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(countver,petallengthver, s=12, color=["green"], marker="o", label = "versicolor")
plt.title("petal_length_scatter")
plt.xlabel("")
plt.ylabel("Petal_Length")
plt.legend()
plt.savefig("petal_length_scatter")
plt.show(block=False)
plt.pause(4)
plt.close("all")
plt.figure(figsize=(12,8))

plt.figure(figsize=(12,8))
plt.scatter(sepalwidthset,sepallengthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(sepalwidthvir,sepallengthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(sepalwidthver,sepallengthver, s=12, color=["green"], marker="o", label = "versicolor")
plt.title("sepal_width_sepal_length_scatter")
plt.xlabel("Sepal_Width")
plt.ylabel("Sepal_Length")
plt.legend()
plt.savefig("sepal_width_sepal_length_scatter")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.scatter(sepalwidthset,petallengthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(sepalwidthvir,petallengthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(sepalwidthver,petallengthver, s=12, color=["green"], marker="o", label = "versicolor")
plt.title("sepal_width_petal_length_scatter")
plt.xlabel("Sepal_Width")
plt.ylabel("Petal_Length")
plt.legend()
plt.savefig("sepal_width_petal_length_scatter")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.scatter(sepalwidthset,petalwidthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(sepalwidthvir,petalwidthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(sepalwidthver,petalwidthver, s=12, color=["green"], marker="o", label = "versicolor")
plt.title("sepal_width_petal_width_scatter")
plt.xlabel("Sepal_Width")
plt.ylabel("Petal_Width")
plt.legend()
plt.savefig("sepal_width_petal_width_scatter")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.scatter(sepallengthset,sepalwidthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(sepallengthvir,sepalwidthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(sepallengthver,sepalwidthver, s=12, color=["green"], marker="o", label = "versicolor")
plt.title("sepal_length_sepal_width_scatter")
plt.xlabel("Sepal_Length")
plt.ylabel("Sepal_Width")
plt.legend()
plt.savefig("sepal_length_sepal_width_scatter")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.scatter(sepallengthset,petalwidthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(sepallengthvir,petalwidthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(sepallengthver,petalwidthver, s=12, color=["green"], marker="o", label = "versicolor")
plt.title("sepal_length_petal_width_scatter")
plt.xlabel("Sepal_Length")
plt.ylabel("Petal_Width")
plt.legend()
plt.savefig("sepal_length_petal_width_scatter")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.scatter(sepallengthset,petallengthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(sepallengthvir,petallengthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(sepallengthver,petallengthver, s=12, color=["green"], marker="o", label = "versicolor")
plt.title("sepal_length_petal_length_scatter")
plt.xlabel("Sepal_Width")
plt.ylabel("Petal_Length")
plt.legend()
plt.savefig("sepal_length_petal_length_scatter")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.scatter(petalwidthset,petallengthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(petalwidthvir,petallengthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(petalwidthver,petallengthver, s=12, color=["green"], marker="o", label = "versicolor")
plt.title("petal_width_petal_length_scatter")
plt.xlabel("Petal_Width")
plt.ylabel("Petal_Length")
plt.legend()
plt.savefig("petal_width_petal_length_scatter")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.scatter(petalwidthset,sepallengthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(petalwidthvir,sepallengthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(petalwidthver,sepallengthver, s=12, color=["green"], marker="o", label = "versicolor")
plt.title("petal_width_sepal_length_scatter")
plt.xlabel("Petal_Width")
plt.ylabel("Sepal_Length")
plt.legend()
plt.savefig("petal_width_sepal_length_scatter")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.scatter(petalwidthset,sepalwidthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(petalwidthvir,sepalwidthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(petalwidthver,sepalwidthver, s=12, color=["green"], marker="o", label = "versicolor")
plt.title("petal_width_sepal_width_scatter")
plt.xlabel("Petal_Width")
plt.ylabel("Sepal_Width")
plt.legend()
plt.savefig("petal_width_sepal_width_scatter")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.scatter(petallengthset,petalwidthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(petallengthvir,petalwidthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(petallengthver,petalwidthver, s=12, color=["green"], marker="o", label = "versicolor")
plt.title("petal_length_petal_width_scatter")
plt.xlabel("Petal_Length")
plt.ylabel("Petal_Width")
plt.legend()
plt.savefig("petal_length_petal_width_scatter")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.scatter(petallengthset,sepalwidthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(petallengthvir,sepalwidthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(petallengthver,sepalwidthver, s=12, color=["green"], marker="o", label = "versicolor")
plt.title("petal_length_sepal_width")
plt.xlabel("Petal_Length")
plt.ylabel("Sepal_Width")
plt.legend()
plt.savefig("petal_length_sepal_width_scatter")
plt.show(block=False)
plt.pause(4)
plt.close("all")

plt.figure(figsize=(12,8))
plt.scatter(petallengthset,sepallengthset, s=12, color=["red"], marker="*", label = "setosa")
plt.scatter(petallengthvir,sepallengthvir, s=12, color=["blue"], marker="x", label = "virginica")
plt.scatter(petallengthver,sepallengthver, s=12, color=["green"], marker="o", label = "versicolor")
plt.title("IRIS Data Set")
plt.xlabel("Petal_Length")
plt.ylabel("Sepal_Length")
plt.legend()
plt.savefig("petal_length_sepal_length_scatter")
plt.show(block=False)
plt.pause(4)
plt.close("all")

df2 = df[["sepal_width", "sepal_length", "petal_length", "petal_width", "species"]]
sns.pairplot(df2, hue = "species")
plt.savefig("pairplot")
plt.show(block=False)
plt.pause(14)
plt.close("all")