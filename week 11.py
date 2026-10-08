import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Iris.csv")
df = df.drop(columns=["Id"])   

print(df.head())
print(df.shape)
df.info()
print(df.describe())
print(df["Species"].value_counts())


df["SepalLengthCm"].hist()
plt.title("Sepal Length Distribution")
plt.show()

sns.boxplot(x="Species", y="PetalLengthCm", data=df)
plt.show()

sns.pairplot(df, hue="Species")
plt.show()