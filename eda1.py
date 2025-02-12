import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("netflix_data.csv")

# Display basic info
print(df.info())
print(df.describe())

# Visualization Example: Movie Ratings Count
sns.countplot(x="rating", data=df)
plt.title("Distribution of Movie Ratings")
plt.xticks(rotation=45)
plt.show()
