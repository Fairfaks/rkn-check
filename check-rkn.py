import requests
import pandas as pd

# 1. Загружаем список заблокированных доменов
print("Загружаем список заблокированных доменов...")
try:
    response = requests.get("https://reestr.rublacklist.net/api/v3/domains/")
    response.raise_for_status()
    blocked_domains = set(response.json())
except requests.RequestException as e:
    print(f"Ошибка при загрузке данных: {e}")
    exit(1)

# 2. Читаем список доменов из файла
try:
    with open("domains.txt", "r", encoding="utf-8") as f:
        input_domains = [line.strip().lower() for line in f if line.strip()]
except FileNotFoundError:
    print("Файл domains.txt не найден.")
    exit(1)

# 3. Проверяем каждый домен
results = []
for domain in input_domains:
    is_blocked = "Да" if domain in blocked_domains else "Нет"
    results.append({"Домен": domain, "Заблокирован в РКН": is_blocked})

# 4. Сохраняем результаты в Excel
df = pd.DataFrame(results)
df.to_excel("проверка_ркн.xlsx", index=False)
print("Готово! Результаты сохранены в файл: проверка_ркн.xlsx")