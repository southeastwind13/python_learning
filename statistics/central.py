import pandas as pd

file_path = 'statistics/Iris.csv'

df = pd.read_csv(file_path)

print(df[['SepalWidthCm', 'SepalWidthCm']].mean())
print(df[['SepalWidthCm', 'SepalWidthCm']].median())