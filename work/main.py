import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
df = pd.read_csv(r"C:\Users\afony\Downloads\archive\PoliceKillingsUs.csv", encoding='cp1252')


# Шаг 1: Найти топ-20 городов
top_cities = df['city'].value_counts().head(20).index

# Шаг 2: Фильтровать данные по топ-20 городам
filtered_df = df[df['city'].isin(top_cities)]

# Шаг 3: Для каждого города визуализировать отношение общего количества записей к количеству записей со значением "B" в колонке race
plt.figure(figsize=(12, 8))

for city in top_cities:
    city_data = filtered_df[filtered_df['city'] == city]
    total_records = len(city_data)
    b_records = len(city_data[city_data['race'] == 'B'])

    plt.bar(city, b_records / total_records, color='orange')

plt.title('Отношение количества записей со значением "B" к общему количеству записей в топ-20 городах')
plt.xlabel('Город')
plt.ylabel('Отношение (B Records / Total Records)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
