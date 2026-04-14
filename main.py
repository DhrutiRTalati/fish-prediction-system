import pandas as pd
df=pd.read_csv("Fish.csv")
print(df.head())
import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(x="Species", y="Weight", data=df)
plt.xticks(rotation=45)
plt.title("Average Weight by Species")
plt.show()
import numpy as np
df["Location"] = np.random.choice(["Coastal", "Deep Sea", "River"], size=len(df))
df["Time"] = np.random.choice(["Morning", "Afternoon", "Evening"], size=len(df))
print(df.head())
sns.barplot(x="Location", y="Weight", data=df)
plt.title("Best Location for Fishing")
plt.show()
sns.barplot(x="Time", y="Weight", data=df)
plt.title("Best Time for Fishing")
plt.show()
sns.countplot(x="Location", hue="Species", data=df)
plt.title("Fish Distribution by Location")
plt.show()