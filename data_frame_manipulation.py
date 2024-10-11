import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
df = pd.read_csv('another_large_random_data.csv')

# Set the seaborn style for better visuals
sns.set(style="whitegrid")

# 1. Age Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=20, kde=True, color='skyblue')
plt.title('Age Distribution of Employees', fontsize=16)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Number of Employees', fontsize=14)
plt.show()

# 2. Annual Salary Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Annual Salary'], bins=30, kde=True, color='green')
plt.title('Annual Salary Distribution', fontsize=16)
plt.xlabel('Salary', fontsize=14)
plt.ylabel('Number of Employees', fontsize=14)
plt.show()

# 3. Employees by Department
plt.figure(figsize=(10, 6))
sns.countplot(y='Department', data=df, palette='Set2', order=df['Department'].value_counts().index)
plt.title('Number of Employees by Department', fontsize=16)
plt.xlabel('Number of Employees', fontsize=14)
plt.ylabel('Department', fontsize=14)
plt.show()

# 4. Salary Distribution by Department
plt.figure(figsize=(10, 6))
sns.boxplot(x='Department', y='Annual Salary', data=df, palette='Set3')
plt.title('Annual Salary Distribution by Department', fontsize=16)
plt.xlabel('Department', fontsize=14)
plt.ylabel('Annual Salary', fontsize=14)
plt.xticks(rotation=45)
plt.show()
