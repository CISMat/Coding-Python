import random as rd

def min(mayusculas):
    x = []
    j=0
    for i in mayusculas: 
        y = str(i.lower())
        x.append(y)
    return(x)


def list_num(a,b):
    x = []
    for i in range(a,b+1):
        x.append(str(i))
    return(x)


def gen_pass():
    mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    minusculas = min(mayusculas)
    simbolos = ['!','@','#','$','%','^','&','*']
    numeros = list_num(0,9)

    caracteres = mayusculas + minusculas + simbolos + numeros

    password = []
    for i in range(20):
        caracter_random = rd.choice(caracteres)
        password.append(caracter_random)
    
    password = ''.join(password)
    return(password)


def run():
    password = gen_pass()
    print('Tu password es: ' + password)


if __name__ == "__main__":
    run()