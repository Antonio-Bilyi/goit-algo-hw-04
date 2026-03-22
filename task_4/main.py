#Імпортуємо необхідні модулі
from input_parser import parse_input
from command_handler import add_contact, change_contact, show_contact

def main():
    #Створюємо словник для збереження контактів
    contacts = {}
    #Вітаємось з користувачем
    print('Welcome to assistant bot!')
    #Запускаємо цикл виконання команд
    while True:
        #Обробляємо введені користвучем дані
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)
        #Програма у разі введення команд 'close', 'exit'
        if command in ['close', 'exit']:
            print('Good bye!')
            break
        #Програма у разі введення команди 'hello'
        elif command == 'hello':
            print('How can I help you ?')
        #Програма у разі введення команди 'add'
        elif command == 'add':
            print(add_contact(args, contacts))
        #Програма у разі введення команди 'change'
        elif command == 'change':
            print(change_contact(args, contacts))
        #Програма у разі введення команди 'phone'
        elif command == 'phone':
            print(show_contact(args, contacts))
                #Програма у разі введення команди 'all'
        elif command == 'all':
            print(contacts)
        #Програма у разі введення невалідної команди        
        else: 
            print('Invalid command')

if __name__ == '__main__':
    main()