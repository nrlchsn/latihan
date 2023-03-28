#my code
Input = input('Please input the secret code: ')
while Input != 'secret':
    print("Sorry, the secret code you entered is incorret. Please try again")
    Input = input('Please input the secret code: ')

print("Welcome!")

#the lecture code
password = ''
while password != "secret"

    password = input('Please enter the password: ')
    if password == "secret":
        print("Welcome!")
    else:
        print("Sorry, the password you entered is incorrect. Please try again")
