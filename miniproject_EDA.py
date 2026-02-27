#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset 
df = pd.read_csv(r"C:\Users\yerol\OneDrive\Desktop\Preeti-Intership\day 20\titanic.csv") 

#Initial Inspection 
df.head()
df.info()
df.describe()

#Phase 2: The Cleanup (Data Preprocessing)
#Check Missing Values
df.isnull().sum()

#Handling Missing Values
# Fill Age with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Drop Cabin column if too many missing values
df.drop(columns=['Cabin'], inplace=True)

# Drop rows where Embarked is missing
df.dropna(subset=['Embarked'], inplace=True)

#Remove Duplicates
df.duplicated().sum()
df.drop_duplicates(inplace=True)

# Univariate Analysis
# Age distribution
plt.figure()
sns.histplot(df['Age'], bins=30)
plt.title("Age Distribution")
plt.show()

# Gender distribution
plt.figure()
sns.countplot(x='Sex', data=df)
plt.title("Gender Distribution")
plt.show()

# passenger class distribution
plt.figure()
sns.countplot(x='Pclass', data=df) # using count plot
plt.title("Passenger Class Distribution")
plt.show()

# Bivariate Analysis
# Survival vs Gender
plt.figure()
sns.countplot(x='Sex', hue='Survived', data=df)# using count plot
plt.title("Survival by Gender")
plt.show()

# Age vs Survival
plt.figure()
sns.boxplot(x='Survived', y='Age', data=df) # using box plot
plt.title("Age vs Survival")
plt.show()

# Correlation Matrix
plt.figure()
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.title("Correlation Matrix")
plt.show()