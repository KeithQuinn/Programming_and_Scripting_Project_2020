#import libraries, keeping all together at the top of the code
import pandas as pd # read CSV file
import matplotlib.pyplot as plt # for plots
import seaborn as sns # for pair plots
from scipy import stats # for normality check

# read in data from file and set up as dataframe
df = pd.read_csv("Fishers IRIS Data Set.csv")

# defining variables
sepalwidth = df["sepal_width"]
sepallength = df["sepal_length"]
petalwidth = df["petal_width"]
petallength = df["petal_length"]
species = df["species"] 

#=============================================  data check  ==============================================

# check the dataset to ensure there are 5 variables and 150 rows of data
print("IRIS Data Set:")
print("")
print(df.loc[:, df.columns != 'Count']) # Count is included in the data set for single variable scatter
# plots. Single variable scatter plots are plotted in univariate analysis, want to ignore "Count" for now.
print("""
==========================================================================================================
""") # The line of === is to make the output easier to read.

print("The number of each species is: ")
print(df["species"].value_counts()) # counting the number of each species, should be 50 of each.
# ignoring "Count" as explained above. 
print("""
==========================================================================================================
""")

#===========================================  data summary  ==============================================

# to output a summary of each variable to a single txt file. As explained previously there is a "Count"
# column in  the data set which has to be ignored here. The method here was to set up a second 
# dataframe (df2) and only include the columns of interest from the original dataframe (df).

df2 = df[["sepal_width", "sepal_length", "petal_length", "petal_width", "species"]]
summary = df2.describe() # provides a summary of the data
print("A summary of the data by variable is provided:")
print("")
print(summary)
with open("summary_of_variables.txt", "w") as f:
    f.write(summary.to_string()) # convert to string to write to text file.

#==========================  checking if data follows a normal distribution  ==========================

shapiro_test_sepal_width = (stats.shapiro(sepalwidth)) # defining the variables for the Shapiro-Wilk test.
shapiro_test_sepal_length = (stats.shapiro(sepallength))
shapiro_test_petal_width = (stats.shapiro(petalwidth))
shapiro_test_petal_length = (stats.shapiro(petallength))
#shapiro returns the test statistic and the p-value, only interested in the p-value and it's located 
#at the second poision in the list, position [1]. If the p-value is greater than 0.05 the data is normal.

if (shapiro_test_sepal_width[1]) >= 0.05:
    print("Sepal Width is Normally Distributed")
else:
    print("Sepal Width is not Normally Distributed")
print("""
""") # Making it easier to read in the output terminal
if (shapiro_test_sepal_length[1]) >= 0.05:
    print("Sepal Lenght is Normally Distributed")
else:
    print("Sepal Lenght is not Normally Distributed")
print("""
""")
if (shapiro_test_petal_width[1]) >= 0.05:
    print("Petal Width is Normally Distributed")
else:
    print("Petal Width is not Normally Distributed")
print("""
""")
if (shapiro_test_petal_length[1]) >= 0.05:
    print("Petal Length is Normally Distributed")
else:
    print("Petal Length is not Normally Distributed")
print("""
==========================================================================================================
""")

#================  histograms as part of univariate analysis  ================

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

#================  boxplots as part of univariate analysis  ================

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

#================  single variable scatter plots as part of univariate analysis  ================

# Setting up a setosa_df, virginica_df and a versicolor_df.

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

# Plotting scatter plots, with each only having one of the four variables of interest.
# Using "Count" as the second variable. This is why count is included in the dataset.
# Part of univariate analysis is to compare one variable at a time for the three species.

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

#================  scatter plots as part of multivariate analysis  ================

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

#================  Seaborn pairplot scatter plots as part of univariate analysis  ================

sns.pairplot(df2, hue = "species")
plt.savefig("pairplot")
plt.show(block=False)
plt.pause(14)
plt.close("all")