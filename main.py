import requests
import csv
import os
from datetime import datetime

url = "https://online-edu.mirea.ru/"
filename = "checks.csv"

try:
    response = requests.get(url, timeout=10)
    status_code = response.status_code
    response_time = round(response.elapsed.total_seconds(), 3)

    print("Сайт:", url)
    print("HTTP-статус:", status_code)
    print("Время ответа:", response_time, "секунд")

    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "url",
                "status_code",
                "response_time_seconds"
            ])

        writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            url,
            status_code,
            response_time
        ])

    print("Результат сохранён в", filename)

except requests.RequestException as error:
    print("Не удалось получить ответ от сайта.")
    print("Причина:", error)
