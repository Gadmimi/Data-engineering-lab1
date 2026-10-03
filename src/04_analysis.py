import s3fs
import pandas as pd

storage_options = {
    "key": "admin",
    "secret": "password12345",
    "client_kwargs": {
        "endpoint_url": "http://localhost:9000"
    }
}

df = pd.read_parquet(
    "s3://airport/processed/flights.parquet",
    storage_options=storage_options
)

# Оставляем только строки, где есть данные за 2026 год
df_clean = df.dropna(subset=['2026']).copy()

# Убираем цифры из названий месяцев (оставляем второе слово после пробела)
df_clean['Период'] = df_clean['Период'].str.split().str[1]

# Считаем прирост за каждый месяц (2026 - 2025)
df_clean['Прирост'] = df_clean['2026'] - df_clean['2025']

# Считаем количество доступных месяцев
months_count = df_clean['Прирост'].count()

# Считаем средний прирост
mean_growth = df_clean['Прирост'].mean()

print("Данные по месяцам с разницей:")
print(df_clean[['Период', '2025', '2026', 'Прирост']])

print(f"\nСредний прирост за {months_count} мес.: {mean_growth:.2f}")
