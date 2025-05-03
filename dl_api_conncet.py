import requests
import pandas as pd
import json
from pathlib import Path
from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"Выгрузка_сотрудники_{current_time}.json"
filenamex = f"Выгрузка_сотрудники_{current_time}.xlsx"


# Жёстко заданные параметры
API_URL = "ecabapi.omgtu.ru:10018/getSecurityInfoEmpl"  # Замените на реальный URL API
API_KEY = "IF2oIR+7jspqpUPLgfGQO5ZihxMOozCygJ2cN90IRQT49u2x"  # Ваш API-ключ
# api_key = os.getenv('CITYAIR_TOKEN')  # or set your api key directly
nameRequest = "getSecurityInfoEmpl"  # Код ключа
#OUTPUT_FOLDER = "T:\Common\Файлы итог"  # Основная папка для сохранения
#OUTPUT_EXCEL = f"T:\Common\Файлы exel/{filenamex}"  # Путь для Excel
#OUTPUT_JSON = f"T:\Common\Файлы json/{filename}"  # Путь для JSON


headers = {
    'GET': '/management/v1/counters HTTP/1.1',
    'Content-Type': 'application/json',
    'up.omgtu.ru': f'{API_KEY}',
}
payload = {'interval': '1'}

if __name__ == "__main__":
    # Получаем данные
    # json_data = get_api_data(API_URL, params)
    """Выполняет GET-запрос и возвращает данные в формате JSON"""
    response = requests.get(API_URL , params=payload, headers=headers)
    print(response)

    if response.status_code == 200:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Запрос выполнен")

    if json_data:
        print('Сохраняем сырой JSON')
        #save_json_data(json_data, OUTPUT_JSON)

        # Сохраняем в Excel
        #save_to_excel(json_data, OUTPUT_EXCEL)


#def get_api_data(url, parameters):



    # try:
    #     print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Отправка запроса...")
    #     response = requests.get(url, params=parameters)
    #     response.raise_for_status()
    #     print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Запрос успешен!")
    #     return response.json()
    # except requests.exceptions.RequestException as e:
    #     print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Ошибка при выполнении запроса: {e}")
    #     return None


# def save_json_data(data, json_path):
#     """Сохраняет сырые JSON-данные в файл"""
#     try:
#         Path(json_path).parent.mkdir(parents=True, exist_ok=True)
#         with open(json_path, 'w', encoding='utf-8') as f:
#             json.dump(data, f, ensure_ascii=False, indent=4)
#         print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] JSON сохранён в: {json_path}")
#         return True
#     except Exception as e:
#         print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Ошибка сохранения JSON: {e}")
#         return False
#
#
# def save_to_excel(data, excel_path):
#     """Сохраняет данные в Excel-файл"""
#     try:
#         Path(excel_path).parent.mkdir(parents=True, exist_ok=True)
#         df = pd.DataFrame(data)
#         df.to_excel(excel_path, index=False)
#         print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Данные сохранены в Excel: {excel_path}")
#         return True
#     except Exception as e:
#         print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Ошибка при сохранении в Excel: {e}")
#         return False


