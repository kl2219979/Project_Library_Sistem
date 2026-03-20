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
