import pandas as pd
df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
print(df.head())

import pandas as pd
pd.options.display.max_columns = 6 # ограничиваем вывод 6 колонками
df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
print(df.describe())


small_df = df[['Age', 'Sex', 'Survived']] # двойные [[]] для множества 
print(small_df.head()) 

df = df['Survived'] #  одинарные [] для одного столбца
print(df.head())

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
df['survived'] = df['Survived'] == 1 # замена 0 и 1 на true и false. Например для колонки "выживший"
print(df.head())