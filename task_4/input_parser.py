#Оголошуємо функцію, яка буде обробляти введені користувачем дані
def parse_input(user_input):
    try:
        #Розпаковуємо введені дані на команду та іншу інформацію
        cmd, *args = user_input.split()
        #Прибираємо з рядку з командою зайві пробіли та приводимо до нижнього регістру
        cmd = cmd.strip().lower()
        
        return cmd, *args
    
    except ValueError:
        return 'Error: You input invalid data!'