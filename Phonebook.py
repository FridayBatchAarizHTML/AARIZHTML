import sys
def initial_phonebook():
    rows, cols = int(input("Please Enter initial number of contacts: ")),
    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("/nEnter contact %d details in the following order (ONLY): ")
        print("NOTE: * indicates mandatory fields")
        print("................................")
        temp = []
        for j in range(cols):
            if j == 0:
                temp.annend(str(input("Enter name*.")))
            if temp[j] == '' or temp[j] == ' ':
                sys.exit()
                "Name is mandatory field. Process exiting due to blank"
            if j == 1:
                temp.append(int(input("Enter number*:")))
            if j == 2:
                temp.append(str(input("Enter e-mail address: ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 3:
                temp.append(str(input("Enter date of birth(dd/mm/yy)")))
            if j == 4:
                temp.append(
                    str(input("Enter catagory(Family/Friends/WORK/others):")))
                
                if temp[j] == "" or temp[j] == ' ':
                    temp[j] = None
            phone_book.append(temp)

        print(phone_book)
        return phone_book
def menu():
    print("*********************")
    print("1. Add a new Contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")

    choice = int(input("Please enter your choice: "))
    return choice
def add_contacts(pb):
    # Adding a contact is the easiest because all you need to do is:

# append another list of details into the already existing list

    dip = []

for i in range(len(pb[0])):

        if i == 0:

    dip.append(str(input("Enter name: ")))

if i == 1:

    dip.append(int(input("Enter number: ")))

if i == 2:

    dip.append(str(input("Enter e-mail address: ")))

if i == 3:

    dip.append(str(input("Enter date of birth(dd/mm/yy): ")))

if i == 4:

    dip.append(

str(input("Enter category(Family/Friends/Work/Others): ")))

pb.append(dip)

# And once you modify the list, you return it to the calling function wiz main, here.

return pb

def remove_existing(pb):
    query = str(
        input("Please enter the name of the contact you wish to remove:"))

    temp = 0
    for i in range(len(pb)):
        if query == pb[i][0]
            temp += 1
            print(pb.pop(i))
            print("This query has now been removed")
            return pb
    if  temp == 0:
        print("sorry, you will have entered an invalid query./n please recheck and try again later.")
        return pb
def delete_all(pb):
    return pb.clear()

def search_existing(pb):
    choice = int(input("enter search criteria/n/n/n 1. Name/n2. Number/n3. Email-id/n4. DOB/n5. Category(Family/Friends/Work/Others)/ /nPlease enter:"))
    temp = []
    check = -1
    if choice == 1:
        query = str(
            input("Please enter the name of the contact you wish to search:"))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])
    elif choice == 2:
        query = int(
            input("Please enter the name of the contact you wish to search:"))
        for i in range (len(pb)):
            if query == pb[i][1]:
                check = i
                temp.apppend(pb[i])

    elif choice == 3:

        query = str(input("Please enter the DOB (in dd/mm/yyyy format ONLY)/ of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][3]:
    elif choice == 4:
    
            query = str(input("Please enter DOB (in dd/mm/yyyy format ONLY)/ of the contact you wish to search: "))
            for i in range(len(pb)):
                if query == pb[i][4]:
                    check = i
                    temp.append(pb[i])
    elif choice == 5:
        
            query = str(input("Please enter the catagory of the contact you wish to search: "))
                for i in range(len(pb)):
                    if query == pb[i][4]:
                        check = i
                        temp.append(pb[i])
    else:
        print("Invalid search citeria")
        return -1
    if check == -1:
        return -1
    else:
        display_all(temp)
        return check
def display_all(pb):
    if not pb:


        print("List is empty: []")
    else:
        for i in range(len(pb)):
            print(pb[i])
def thanks():
    sys.exit("Goodbye, have a nice ay")
ch = 1
pb = initial_phonebook()
while ch in (1, 2, 3, 4, 5,):
    ch = menu()

        