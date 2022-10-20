#My Contacts by Adi

#Inizialize the list
contacts = [
    {'name': "Tim", 'phonenum': "587 - 535 - 3532", 'email': "tim@gmail.com"},
    {'name': "Kat", 'phonenum': "780 - 421 - 7654", 'email': "kat@gmail.com"},
    {'name': "Bob", 'phonenum': "825 - 234 - 5321", 'email': "bob@gmail.com"}
]

#Function to test if In list
# Index Of
def indexOf(aList, item):
    for index, element in enumerate(aList):
        if element == item:
          return index
    return -1

#Set Loop True
ProgramLoop = True

#Start Looping
while ProgramLoop:

  #Options To pick From
    print("OPTION 1: Display Contact Names")
    print("OPTION 2: Search for Contact")
    print("OPTION 3: Edit Contact")
    print("OPTION 4: New Contact")
    print("OPTION 5: Remove Contact")
    print("OPTION 6: Exit")

    #Input From The user
    userInput = input("Pick your Option:")

    #Option 1 - Display Contact Names
    if(userInput == "1"):
        for i in range(len(contacts)):
            print(contacts[i]["name"])
    

    #Option 2 - Search for Contact
    elif(userInput == "2"):
        check = 0
        contactinput = input("Please enter Name of your contact\n")
        for i in range(len(contacts)):    
            if contactinput == contacts[i]["name"]:
                print(contactinput, "is in the list. Here is the information:")
                print(contacts[i]["name"] + "\n" + contacts[i]["phonenum"] + "\n" + contacts[i]["email"])
                check = 0
                break
            else:
                check = -1
        if check == -1:
            print("Contact not found")


    #Option 3 - Edit Contact
    elif(userInput == "3"):
        check = 0
        contactinput = input("Please enter Name of your contact:\n")
        for i in range(len(contacts)):
            if contactinput == contacts[i]["name"]:
                print("Please update the Name, Phone Number, and email:")
                newname = input("What is the new name:\n")
                newnum = input("What is the new phone number:\n")
                newemail = input("What is your new email?:\n")
                contacts[i]["name"] = newname
                contacts[i]["phonenum"] = newnum
                contacts[i]["email"] = newemail
                print("Here is your new information:")
                print(contacts[i]["name"] + "\n" + contacts[i]["phonenum"] + "\n" + contacts[i]["email"])
                check = 0
                break
            else:
                check = -1
        if check == -1:
            print("Contact not found")
       

    #Option 4 - New Contact
    elif (userInput == "4"):
        check = 0
        namecontact = input("Please enter the name of the Contact you want to add:\n")
        for i in range(len(contacts)):
            if namecontact == contacts[i]["name"]:
                check = -1
                break
            else:
                phonenum = input("What is your phone number?:\n")
                email = input("What is your email?:\n")
                contacts.append({'name': namecontact, 'phonenum': phonenum, 'email': email})
                print("Contact has been added")
                check = 0
        if check == -1:
            print("Contact Already exists")


    #Option 5 - Remove Contact
    elif(userInput == "5"):
        check = 0
        namecontact = input("Please enter the name you want to remove:\n")
        for i in range(len(contacts)):
            if namecontact in contacts[i]["name"]:
                contacts.pop(i)
                check = 0
            else:
                check = -1
                break
        if check == -1:
            print("Contact nor found")


    #Option 6 - End Loop
    elif(userInput == "6"):
        Programloop = False
        break 

