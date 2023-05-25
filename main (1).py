#Basic Log In/Sign Up Form 
print("Hello and welcome to our website! please log in below! \n")


#While loop to keep going until the break

while True:
    name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")
    print('\n')

#Setting variables and conditions, age checker.

    if age < 13:
        print("You aren't old enough to visit our site! The minimum age is 13!")
        break

    print(f'Hello {name} {last_name} you are {age} years old and your email is {email}!\n')


#Verifying info to be correct
    
    verification = input("Is the following information correct? (Y/N): ").upper()
    if verification == 'Y':
        print(f"Perfect! Welcome to our website! We hope you enjoy your experience here {name}! \n")
        break
    elif verification == 'N':
        print("Sorry about that! Please try again :/\n")
        continue
    else:
        print("Sorry, you didn't put the following options Y/N! ERROR :/\n")
        continue
        break

    

