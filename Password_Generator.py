import string
import secrets

def pass_gen(length):
    
    symbols = '!@#$%&*'
    choices = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(choices) for i in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)):
            break
    symbs = secrets.choice(symbols) + secrets.choice(symbols)
    print(password + symbs)


pass_gen(12)