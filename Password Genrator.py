import random
import string

pas=list(string.ascii_letters + string.digits + "!@#$%^&*")

def Password_Generator():
    n=int(input("Enter The Lenght Of The Password:"))
    random.shuffle(pas)

    password=[]
    for i in range(pas):
        password.append(random.choice(pas))

        random.shuffle(pas)

        print("Your Password Is:".join(password))

        Password_Generator()


