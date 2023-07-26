"""
    Continuación de la agenda.
        Escribir un programa que vaya solicitando al usuario que ingrese nombres.
        a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar
        el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
        b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
        El usuario puede utilizar la cadena ”*”, para salir del programa.
"""


def is_on_phone_book(name, phone_book):
    
    boolean = False

    if name in phone_book:
        boolean = True

    return boolean


def add_number(name,phone_book):
    
    new_number = input("Ingrese el número: ")

    phone_book[name] = new_number


def main():

    phone_book = {"Joel": "1558384705", "Sol": "1559302710"}
    condition = True

    while condition:
        name = input("\nIngrese un nombre('*' para salir): ")

        if name == "*":
            condition = False
        else:
            boolean = is_on_phone_book(name, phone_book)

            if boolean:
                print("El nombre se encuentra en la agenda.")
                print(f"Nombre: {name}, Telefono: {phone_book[name]}")
                condition2 = input("¿Desea modificar el número?.('Y'=si/'N'=no): ")
                
                if condition2 == 'Y':
                    add_number(name,phone_book)
            else:
                print("El nombre no se encuentra en la agenda, ingrese su número y se agregara.")
                add_number(name,phone_book)




main()