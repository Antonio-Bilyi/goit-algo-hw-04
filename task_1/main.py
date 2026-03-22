#Імпортуємо необіхдні нам модулі
from pathlib import Path

#Оголошуємо функцію, яка приймає шлях до текстового файлу та повертає кортеж із двох чисел
def total_salary(path: str) -> tuple[int, int]:
    #Визначаємо директорію, де знаходиться файл скрипту
    current_dir = Path(__file__).parent
    try:
        #Відкриваємо та читаємо файл
        with open(current_dir / path, 'r', encoding='utf-8') as fh:
            #Створюємо змінні лічильники
            users = 0
            total = 0
            #Цикл, який буде проходитись по кожному рядку
            for el in fh:
                #Перевіряємо чи не є елемент порожнім рядком
                if not el.strip() : continue
                #Розділяємо дані у кожному рядку
                element = el.strip().split(',')
                #Перевіряємо чи маються у рядку усі необхідні нам значення
                if len(element) < 2: continue
                #Беремо заробітню плату з рядку та приводимо її до числа (можна також float)
                user_salary = int(element[1].strip())
                #Вираховуємо загальну суму ЗП
                total += user_salary
                #Додаємо на кожній ітерації одиницю до лічильника працівників
                users += 1          
        #Вираховуємо середню ЗП
        average = 0
        if users > 0: average = total // users

        #Повератємо кортеж із двох чисел: загальна сума ЗП та середня ЗП
        return (total, average)

        
    except FileNotFoundError:
        print('Файл відсутній або пошкоджений')
        return (0, 0)
    

total, average = total_salary('data.txt')
print(f'Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}')