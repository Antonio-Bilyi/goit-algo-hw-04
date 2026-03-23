#Оголошуємо функцію, яка буде додавати контаки до списку
def add_contact(args, contacts):
    #Перевіряємо чи корустувач передав необхідні дані, а саме ім'я + номер телефону
    if len(args) < 2:
        return 'Invalid format: please input name and phone'

    name, phone = args
    #Перевіряємо чи містяться у номері тільки цифри
    if not phone.isdigit():
        return 'Phone must include only numbers'
    #Перевіряємо чи є вже контакт у списку з таким іменем
    if name in contacts:
        return f'Contact {name} already exists! Enter new contact'

    contacts[name] = phone

    return 'Contact added.'

#Оголошуємо функцію, яка буде змінювати номер контакту
def change_contact(args, contacts):
    #Перевіряємо чи корустувач передав необхідні дані, а саме ім'я + номер телефону
    if len(args) < 2:
        return 'Invalid format: please input [name] and [phone]'

    name, new_phone = args
    #Перевіряємо чи є контакт у словнику
    if name not in contacts:
        return f'Contacts {name} not found! Please create this contact'
    #Перевіряємо чи вірно введено номер
    if not new_phone.isdigit():
        return 'Phone must include only numbers'

    contacts[name] = new_phone
    
    return 'Contact changed.'

#Оголошуємо функцію, яка буде виводити у консоль номер конкертного контакту
def show_contact(args, contacts):
    #Перевіряємо чи передано користувачем ім'я
    if not args:
        return 'Please enter a username'

    name = args[0]
    #Перевіряємо чи є такий контакт та виводимо його номер
    if name in contacts:
        phone = contacts[name]

        return f'Contact {name} has phone number {phone}'
    
    else:
        return f'Contact {name} not found'

def all_contacts(contacts):

    return (contacts)

        
