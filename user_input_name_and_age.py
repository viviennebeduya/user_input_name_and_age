# user input name and age
user_input = {}
# print error input=valid
# --define valid name and valid age
while True:
    while True:
        try:
            name = str(input("Input a name: "))
            age = int(input("Input an age: "))
        
            user_input[name] = {
                "age": age
            }

            print (user_input)

            retry = input ("Would you like to input another?")
            break

        except:
            print ("Input invalid.")
            
    if retry == "no":
        break
    elif retry != "yes":
        print ("Invalid Input.")
# store infos to array
# every input, ask if it wants another entry
    # Yes = ask again for input
        # Until the user says No
    # No = display the name and age of the oldest person

