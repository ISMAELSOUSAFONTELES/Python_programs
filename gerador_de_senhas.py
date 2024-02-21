import secrets
import string
spec = "!@#$%&*()_+=-?/;:[{]}|"
pswddgts = 2*string.digits + string.ascii_letters + spec


def psswd_gen():
    
    while True:
        password = ''
        upper = num = lower = special = False
        for i in range(12):
            a = secrets.choice(pswddgts)
            password += a
            if a.islower():
                lower = True
            if a.isupper():
                upper = True
            if a.isnumeric():
                num = True
            if a in spec:
                special = True
        if upper is True and lower is True and num is True and special is True:
            return password
        
        
print(psswd_gen())