from pathlib import Path

#Оголошуємо функцію, яка приймає шлях до текстового файлу та повертає кортеж із двох чисел
def total_salary(path):

    current_dir = Path(__file__).parent
    try:

        with open(current_dir / path, 'r', encoding='utf-8') as fh:

            users = 0
            total = 0

            for el in fh:
                #Перевіряємо чи не є елемент порожнім рядком
                if not el.strip() : continue

                element = el.strip().split(',')
                #Перевіряємо чи маються у рядку усі необхідні нам значення
                if len(element) < 2: continue

                user_salary = float(element[1].strip())

                total += user_salary
    
                users += 1          

        average = 0
        if users > 0: average = total / users


        return (total, average)

        
    except FileNotFoundError:
        print('Файл відсутній або пошкоджений')
        return (0, 0)
    

total, average = total_salary('data.txt')
print(f'Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}')