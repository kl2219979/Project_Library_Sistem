from models import books
from validations import validation_update, validation_book_name, validation_book_year, validation_book_author, validation_status, validation_erase
# Funciones 

def register_book():
    """This function requests user data such as (tittle, year, author) and then adds it to the dictionary as a list"""
    
    tittle = validation_book_name()
    year = validation_book_year()
    author = validation_book_author()
    status = validation_status()
    return {
        "tittle": tittle,
        "year": year,
        "author": author,
        "status": status
    }


def show_books():
    """This function displays the tittles in the list"""
    
    for i, each_book in enumerate(books):
        print(f"{i+1} - tittle: {each_book['tittle']}, year: {each_book['year']}, author: {each_book['author']}, status: {each_book['status']}")
    
    
# Funtions
def update_book():
    show_books()
    selected_book= validation_update() #Here goes a validations
    while True:
        try:
            update_choice=int(input("\nWhat do you want to update?:\n1.Tittle\n2.Year\n3.Author\n4.Select another book\n5.Exit\nType the number of what you want to update: "))
            if update_choice== 1:
                new_tittle= input("Type the new tittle: ")
                books[selected_book-1]["tittle"]= new_tittle
                print(f"\n\t***UPDATED BOOK***\nTittle: {books[selected_book-1]["tittle"]}, Year: {books[selected_book-1]["year"]}, Author: {books[selected_book-1]["author"]}, Status: {books[selected_book-1]["status"]}")
            elif update_choice== 2:
                new_year= input("Type the new year: ")
                books[selected_book-1]["year"]= new_year
                print(f"\n\t***UPDATED BOOK***\nTittle: {books[selected_book-1]["tittle"]}, Year: {books[selected_book-1]["year"]}, Author: {books[selected_book-1]["author"]}, Status: {books[selected_book-1]["status"]}")       
            elif update_choice==3:
                new_author= input("Type the new author: ")
                books[selected_book-1]["author"]= new_author
                print(f"\n\t***UPDATED BOOK***\nTittle: {books[selected_book-1]["tittle"]}, Year: {books[selected_book-1]["year"]}, Author: {books[selected_book-1]["author"]}, Status: {books[selected_book-1]["status"]}")       
            elif update_choice==4:
                return(update_book())
            elif update_choice==5:
                print("\n\t***It was a pleasure to help you!***")
                break
            else:
                print("\n\t----Type a valid option----")
        except ValueError:
            print("\n\t----Type a valid option----")

def book_status():
    
    while True: 
        show_books()
        try:
            selected_book= int(input("\nWhich book do you want to update its status(select the number): "))
            if 0 < selected_book <= len(books):
                new_status= validation_status()
                books[selected_book-1]["status"]= new_status
                print(f"\n\t***UPDATED BOOK***\nTittle: {books[selected_book-1]['tittle']}, Year: {books[selected_book-1]['year']}, Author: {books[selected_book-1]['author']}, Status: {books[selected_book-1]['status']}")
                break
            else:
                print("\nError, try again")
        except ValueError:
            print("\n\t----Type a valid option----") 


def erase_book():
    while True:
        show_books()
        eliminate= validation_erase()
        books.pop(eliminate-1)
        print("The new list is: ")
        show_books()
        if not books:
            print("You dont have any book")
            break
        else:
            eliminate_another=(input("Eliminate another book? y/n: ")).lower()
            if eliminate_another == "y":
                return erase_book()
            elif eliminate_another =="n":
                break
            else:
                print("Invalid option. Try again")



