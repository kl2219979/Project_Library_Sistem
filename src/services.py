
# Funciones 

def register_book():
    """This function requests user data such as (tittle, year, author) and then adds it to the dictionary as a list"""
    
    tittle = input("Enter the book tittle: ")
    year = int(input("Enter the year of the book: "))
    author = input("Enter the book's author:")
    return {
        "tittle": tittle,
        "year": year,
        "author": author
    }


def show_books():
    """This function displays the tittles in the list"""
    
    for i, each_book in enumerate(books):
        print(f"{i+1} - tittle: {each_book['tittle']}, year: {each_book['year']}, author: {each_book['author']} ")
    
    

