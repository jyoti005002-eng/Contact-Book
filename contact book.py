import json  
# print("CONTACT BOOK !! ")
# print("Click 1. to Add contact ")
# print("Click 2. to view all contacts")
# print("Click 3. to search contact")
# print("Click 4. to update Contact")
# print("Click 5. to Delete Contact")
# print("Click 6. to Exit ")

# choice = int(input("Choose the option from above : "))


with open("contact book.json" , "r") as file:
      contact = json.load(file)

def show_menu():
        print("CONTACT BOOK !! ")
        print("Click 1. to Add contact ")
        print("Click 2. to view all contacts")
        print("Click 3. to search contact")
        print("Click 4. to update Contact")
        print("Click 5. to Delete Contact")
        print("Click 6. to Delete all Contacts")
        print("Click 7. to Exit ")


def add_contact():
        
        name = input("Enter contact name : ")
        number = input("Enter contact number : ")
        email = input("Enter their email : ")

        new_contact = {
               "name" : name,
               "number" : number , 
               "email" : email
        }

        contact.append(new_contact)
        save_contacts()

        print("Contact Saved !! ")

def view_all_contact ():
        if not contact:
                print("No contact yet...")
                return
        else:
                print("Yours contacts are : ")
                for index , person in enumerate(contact ,start = 1):
                    print(index , person["name"] )



def search_contact():
       if not contact:
              print("No contacts avaiable...")
              return
       else:
              print("Your contacts are : " )
              view_all_contact()

              print("You can search any contact here !! ")
              index = int(input("Enter their idex number : "))

              if( 1 <= index <= len(contact)):
                     person = contact[index-1]
                     print("Name :" , person["name"])
                     print("Number :" , person["number"])
                     print("Email :" , person["email"])

              else:
                     print("NOT FOUND!!") 

def update_Contact():
       if not contact:
              print("No contact available...")
              return
       else:
                print("Your contacts are : ")
                view_all_contact()

                index = int(input("Enter the index number of contact you want to edit :"))
                if( 1<= index <= len(contact)):
                    print("Current deitals : ")
                    person = contact[index-1]
                    print("Name : " , person["name"] )
                    print("Number : " , person["number"])
                    print("Email: " , person["email"])

                    print( "To update them .. enter details below : ")
                    name = input("Enter name : ")
                    number = input("Enter number : ")
                    email = input("Enter email : ")

                    updated_contact = {
                           "name" : name,
                           "number" : number,
                           "email" : email
                    }

                    contact[index-1] = updated_contact
                    save_contacts()
                    print(updated_contact)

                else:
                       print("Invalid Input !!")

def delete_contact():
       if not contact:
              print("No contact available...")
       else:
            print("Contacts are : ")
            view_all_contact()

            print("To delete any contact enter their index number :")
            index =int(input("Enter the index of contact you want to delete : "))

            if(1<= index <= len(contact)):
                print("DELETING...")
                person = contact[index-1]
                contact.remove(person)
                save_contacts()
                print("Successfully Deleted !! ")

 #  or instead of last two line i can write .. contact.pop(index-1) so i can remove the item at that list position directly 

            else:
                   print("Invalid input !!")

def delete_all_contact():
      if not contact:
            print("No contact available...")
      else:
            print("SUCCESSFULLY DELETED...")
            contact.clear()
            save_contacts()

def save_contacts():
      with open("contact book.json" , "w") as file:
            json.dump(contact , file , indent = 4)


while True :

      show_menu()
      choice = int(input("Choose the option from above : "))

      if(choice == 1 ):
             add_contact()
      elif(choice == 2 ):
             view_all_contact()
      elif(choice == 3):
            search_contact()
      elif(choice == 4):
            update_Contact()
      elif(choice == 5):
            delete_contact()
      elif(choice == 6):
            delete_all_contact()
      elif(choice == 7):
            print("EXITING....")
            break
      else:
       print("Invalid Input !!")



