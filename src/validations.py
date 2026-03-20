# validaciones
def validacion_nombre_libro():
    books_name = input("Enter Name of the book: ")
    if books_name.strip().replace(" ", "").isalpha():
        return books_name
    else:
        return validacion_nombre_libro()
    

def validacion_año_libro():
        try:
            book_year = int(input("Enter Name of the year of the book: "))
            if 0 <= book_year <= 2026: 
                return book_year
            else:
                print("invalid option")
        except ValueError:
            print("invalid option")
            return validacion_año_libro()       

def validacion_autor_libro():
    autor = input(" Enter name of the author: ")
    if autor.strip().replace(" ", "").isalpha():
        return autor
    else:
        return validacion_autor_libro()

def validacion_opcion_menu():
    try:
        opcion_menu = int(input("Ingresa una opcion en el menu: "))
        if  0 <= opcion_menu <= 6:
            return opcion_menu
        else:
            print("Wrong option")
    except ValueError:
        print("Wrong option")
        return validacion_opcion_menu()

