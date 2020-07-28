# Passwort Generator
import secrets
import string

print("If You want a Save password the password should be around 13 digits long")
C = input("How long should your Password be?")
C = int(C)


def RDM():
    c = ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(C))

    file = open("YourPasswords.txt", "a")
    file.write(f'Your Password is {c}\n')
    file.close()
    return c


RDM()

