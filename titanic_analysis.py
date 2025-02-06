import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = sns.load_dataset('titanic')

# Display the first 5 rows of the data
print(df.head())

# Display the number of rows and columns in the data
print ("First 5 rows of the dataset")
print(df.head())

#basic information about the dataset
print("n\Dataset Information")
print(df.info())

# Summary Statistics
print("n\Summary Statistics")
print(df.describe())

