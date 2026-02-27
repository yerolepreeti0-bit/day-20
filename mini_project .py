# MINI PROJECT 3
# Student Performance & Academic Risk Analyzer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
import sqlite3

# 1. Load Dataset
df = pd.read_csv("StudentsPerformance.csv")
print("\nFirst 5 Rows:")
print(df.head())


# 2. Data Cleaning
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Distribution of Math Scores
plt.figure()
sns.histplot(df['math score'], kde=True)
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.show()


# 4. Distribution of Reading Scores
plt.figure()
sns.histplot(df['reading score'], kde=True)
plt.title("Distribution of Reading Scores")
plt.xlabel("Reading Score")
plt.ylabel("Frequency")
plt.show()


# 5. Distribution of Writing Scores
plt.figure()
sns.histplot(df['writing score'], kde=True)
plt.title("Distribution of Writing Scores")
plt.xlabel("Writing Score")
plt.ylabel("Frequency")
plt.show()

# 6. Skewness
print("\nSkewness:")
print("Math Score Skewness:", df['math score'].skew())
print("Reading Score Skewness:", df['reading score'].skew())
print("Writing Score Skewness:", df['writing score'].skew())


# 7. Mean, Median, Standard Deviation
print("\nStatistics:")
print("\nMath Score")
print("Mean:", df['math score'].mean())
print("Median:", df['math score'].median())
print("Standard Deviation:", df['math score'].std())
print("\nReading Score")
print("Mean:", df['reading score'].mean())
print("Median:", df['reading score'].median())
print("Standard Deviation:", df['reading score'].std())
print("\nWriting Score")
print("Mean:", df['writing score'].mean())
print("Median:", df['writing score'].median())
print("Standard Deviation:", df['writing score'].std())


# 8. Z-Score Detection (Low Performers in Math)
df['z_score_math'] = zscore(df['math score'])
low_performers = df[df['z_score_math'] < -2]
print("\nNumber of Extremely Low Performers (Math):", len(low_performers))


# 9. % of Students Above 1 Std Deviation (Math)
mean_math = df['math score'].mean()
std_math = df['math score'].std()
above_1_std = df[df['math score'] > (mean_math + std_math)]
percentage = (len(above_1_std) / len(df)) * 100
print("\n% of Students Above 1 Std Deviation (Math):", round(percentage,2), "%")


# 10. SQL Part
conn = sqlite3.connect("student.db")
df.to_sql("students", conn, if_exists="replace", index=False)
query = """
SELECT gender, AVG([math score]) as avg_math
FROM students
GROUP BY gender
"""
group_result = pd.read_sql(query, conn)
print("\nGROUP BY Gender (Average Math Score):")
print(group_result)
conn.close()


# 11. Gender Comparison (Boxplot)
plt.figure()
sns.boxplot(x='gender', y='math score', data=df)
plt.title("Math Score Comparison: Male vs Female")
plt.show()
print("\nProject Completed Successfully ✅")