# Funtions
def update_book():
    selected_book= int(input("\nWhich book do you want to update (select the number): "))#Here goes a validations
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
        except ValueError:
            print("\n\t----Type a valid option----")

def book_status():
    while True: 
            try:
                selected_book= int(input("\nWhich book do you want to update its status(select the number): "))
                if 0 < selected_book <= len(books):
                    new_status=input("Type the new status (Available or Borrowed): ").lower()
                    if new_status == "available" or new_status == "borrowed":
                        books[selected_book-1]["status"]= new_status
                        print(f"\n\t***UPDATED BOOK***\nTittle: {books[selected_book-1]["tittle"]}, Year: {books[selected_book-1]["year"]}, Author: {books[selected_book-1]["author"]}, Status: {books[selected_book-1]["status"]}")
                        break
                    else:
                        print("\n||||----Not a valid option :( , start again----|||")
                else:
                    print("\nError, try again")
            except ValueError:
                print("\n\t----Type a valid option----") 


