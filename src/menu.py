from services import register_book, show_books, update_book, book_status, erase_book
from validations import validation_menu_option
from models import books
# Menu

def menu():
    print("\n\t|||--HI! WELCOME TO THE LIBRARY--|||")
    while True:
        print("Menu options: ")
        print("1 . Add book")
        print("2 . List books")
        print("3 . Update book")
        print("4 . Delete book")
        print("5 . Update book status")
        print("6 . Exit")
        entrada_opcion = validation_menu_option()
        match entrada_opcion:
            case 1: 
                book = register_book()
                books.append(book)
            case 2: 
                if not books:
                    print("You dont have any book")
                else:
                    show_books()
            case 3: 
                if not books:
                    print("You dont have any book")
                else:
                    update_book()
            case 4: 
                if not books:
                    print("You dont have any book")
                else:
                    erase_book()
            case 5: 
                if not books:
                    print("You dont have any book")
                else:
                    book_status()
            case 6: 
                print("Thank you for using our library system, see you later!")
                break
            case _:
                print("Wrong option, try again")

    