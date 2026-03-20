# Menu

def menu():
    while True:
        print("Menu options: ")
        print("1 . Agregar")
        print("2 . Listar")
        print("3 . Actualizar")
        print("4 . Eliminar")
        print("5 . Disponibilidad")
        print("6 . Salir")
        entrada_opcion = int(input("Escoge una opcion: "))
        match entrada_opcion:
            case 1: 
                print("agregar")
            case 2: 
                print("Listar")
            case 3: 
                print("Actualizar")
            case 4: 
                print("Eliminar")
            case 5: 
                print("Disponibilidad")
            case 6: 
                print("Saliendo")
                break
            case _:
                print("Eliga una opcion correcta")
menu()
    