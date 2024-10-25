# user input name and age
# print error input=valid
# --define valid name and valid age
try:
    name = str(input("Input a name: "))
    age = int(input("Input an age: "))
except:
    print ("Input invalid.")
# store infos to array
# every input, ask if it wants another entry
    # Yes = ask again for input
        # Until the user says No
    # No = display the name and age of the oldest person

