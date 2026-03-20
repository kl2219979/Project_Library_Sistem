from models import books

# validaciones
def validation_update():
    try: 
        selected_book= int(input("\nWhich book do you want to update (select the number): "))
        if 0 < selected_book <= len(books):
            return selected_book
        else: 
            print("\nError, try again")
            return validation_update()
        
    except ValueError:
        print("Error, try again")
        return validation_update()
    
def validation_book_name():
    books_name = input("Enter Name of the book: ")
    if books_name.strip().replace(" ", "").isalpha():
        return books_name
    else:
        return validation_book_name()

def validation_book_year():
        try:
            book_year = int(input("Enter the year of the book: "))
            if 0 <= book_year <= 2026: 
                return book_year
            else:
                print("invalid option")
                return validation_book_year()
        except ValueError:
            print("invalid option")
            return validation_book_year()       

def validation_book_author():
    autor = input("Enter name of the author: ")
    if autor.strip().replace(" ", "").isalpha():
        return autor
    else:
        return validation_book_author()

def validation_menu_option():
    try:
        opcion_menu = int(input("Enter the menu option: "))
        if  0 <= opcion_menu <= 6:
            return opcion_menu
        else:
            print("Wrong option")
    except ValueError:
        print("Wrong option")
        return validation_menu_option()
    
def validation_status():
    new_status=input("Type the new status (Available or Borrowed): ").lower()
    if new_status == "available" or new_status == "borrowed":
        return new_status
    else:
        print("\n||||----Not a valid option :( , start again----|||")
        return validation_status()

