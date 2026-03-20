# Funciones 

def erase_book():

    
        for i,j in enumerate(books,start=1):
            print (f"{i}- {books['book']} | {books['year']} | {books['author']}")

        while True:
            eliminate=int(input("What book want to eliminate? "))
            books.pop(eliminate-1)
            print("The new list is: ")
            for i,books in enumerate(books,start=1):
                print (f"{i}- {books['book']} | {books['year']} | {books['author']}")
            
            
            if not books:
                print("No hay libros xd")
                break
            else:
                eliminate_another=(input("Eliminate another book? y/n: ")).lower()
                if eliminate_another == "y":
                    return erase_book()
                elif eliminate_another =="n":
                    break
                else:
                    print("Invalid option. Try again")



