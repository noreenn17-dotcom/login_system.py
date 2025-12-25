username = input('enter your username: ')
password = int(input('Enter your password: '))
saved_username = 'Noreen12'
saved_password = 12344874
if username == saved_username and password == saved_password:
    print('login sucessfully')
elif username == saved_username and password != saved_password:
    print('wrong password')
elif username != saved_username and password == saved_password:
    print('wrong')
else:
    print('Invalid username and password')