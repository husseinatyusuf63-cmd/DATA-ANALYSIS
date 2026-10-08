import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Iris.csv")

print(df.head())
print(df.describe())
print(df["Species"].value_counts())

# Histogram
df["PetalLengthCm"].hist()
plt.title("Petal Length")
plt.show()

# Scatter plot
sns.scatterplot(x="SepalLengthCm", y="PetalLengthCm", hue="Species", data=df)
plt.title("Sepal Length vs Petal Length")
plt.show()