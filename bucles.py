def run(num,LIMITE):

    i = 0
    potencia_2 = num**i
    while potencia_2 < LIMITE:
        print(str(num)+' elevado a '+ str(i) + ' es igual a ' + str(potencia_2))
        i = i+1
        potencia_2 = num**i


def tabla(num,lim):
    print("Esta es la tabla del: " + str(num))
    for i in range(1,int(lim)+1):
        val = i*num
        print(str(num) + " multiplicado por: " + str(i) + " Es igual a:  " + str(val))


if __name__ == "__main__":
    num = int(input('Ingrese el numero base: '))
    lim = int(input('Ingrese el numero limite: '))
    run(num,lim)
    tabla(num, lim)

