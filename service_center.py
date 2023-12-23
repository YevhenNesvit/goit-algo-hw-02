import queue
import time
import random

# Створення черги заявок
request_queue = queue.Queue()

def generate_request():
    # Генерування нової заявки і додавання до черги
    if random.random() < 0.5:
        time.sleep(2)
        request_id = str(time.time())  # Унікальний номер заявки
        request_queue.put(request_id)
        print(f"Заявка {request_id} створена")

def process_request():
    # Якщо черга не пуста, обробити заявку
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Обробка заявки {request_id}")

        # Симуляція тривалості обробки
        time.sleep(2)
    else:
        # Якщо черга пуста, вивести повідомлення
        print("Черга пуста")

# Головний цикл програми
try:
    while True:
        # Виконати generate_request() для створення нових заявок
        generate_request()

        time.sleep(2)

        # Виконати process_request() для обробки заявок
        process_request()
except KeyboardInterrupt:
    # Переривання програми при натисканні Ctrl+C
    print("Програма завершена")