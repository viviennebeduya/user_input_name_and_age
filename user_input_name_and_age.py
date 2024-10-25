# array
user_input = {}
# initialize oldest name,age
oldest_age = 0
oldest_name = None

# users input name and age
while True:
    while True:
# define valid name and valid age
        try:
            name = str(input("Input a name: "))
            age = int(input("Input an age: "))
        
            user_input[name] = {
                "age": age
            }
#identification of oldest
            if age > oldest_age:
                oldest_name = name
                oldest_age = age

            print (f"\nCurrent Directory: \n {user_input}.")
# ask if user wants another entry
            while True:
                retry = input ("Would you like to input another (yes/no)? ")
                if retry == "no":
                    break
                elif retry == "yes":
                    break
                else:
                    print('Input is invalid. Please enter if "yes" or "no"')
            break
# print error input=valid
        except:
            print ("Input Invalid. Please input valid name and age.")
    if retry == "no":
        break

print (f"The oldest person is {oldest_name} at the age of {oldest_age}.")

