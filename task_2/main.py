from pathlib import Path

#Оголошуємо функцію, яка приймає шлях до текстового файлу та повертає список словників
def get_cats_info(path: str) -> list[dict]:

    current_dir = Path(__file__).parent

    try:

        with open(current_dir / path, 'r', encoding='utf-8') as fh:

            cats_list = []

            for el in fh:
                #Перевіряємо чи не є елемент порожнім рядком
                if not el.strip() : continue

                element = el.strip().split(',')
                #Перевіряємо чи маються у рядку усі необхідні нам значення
                if len(element) < 3 : continue

                cat_dict = {'id': element[0], 'name': element[1], 'age': element[2]}

                cats_list.append(cat_dict)

            return cats_list
    #Обробляємо виняток у разі коли файл відсутній або пошкоджений    
    except FileNotFoundError:
        print('Файл відсутній або пошкоджений')
        return []

cats_info = get_cats_info('data_cats.txt')

for cat in cats_info:
    print(cat)