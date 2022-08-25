import pandas as pd

данные = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
таблица = данные[0]
print(таблица)
выборочная_таблица = таблица[['Symbol', 'Security']]
print(выборочная_таблица)
фильтрованная_таблица = таблица[таблица['Security'] == 'Apple']
print(фильтрованная_таблица)
список_столбцов = таблица.info() 
print(список_столбцов)



# ---------------------------------------------------------------------------------
print("-"*50)
# для обхода ошибки необходимо сделать запрос, указав в хедере данные о юзерагенте
import pandas as pd
import requests
import matplotlib.pyplot as plt

# стандартный header
хедер ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# ссылки на таблицы
url_link = 'https://finance.yahoo.com/quote/TSLA/analysis?p=TSLA'

# делаем запрос
запрос = requests.get(url_link, headers=хедер)
таблица = pd.read_html(запрос.text)

# выведем таблицу
print(таблица[0]) 

# выведем график
таблица = таблица[0]
таблица = таблица[таблица['Earnings Estimate'] == 'Avg. Estimate']
таблица.plot(kind='bar')
plt.show()
# plt.savefig('график.png')