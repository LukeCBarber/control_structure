# Password Verification

password = 'bobcat'

while True:
    password_entered = input('Enter your password: ')
    if password_entered == password:
        break
    else:
        print('Access denied. Try Again')
        
print('Access granted')
