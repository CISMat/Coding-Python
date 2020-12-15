# def es_primo(num):
#     contador = 0
#     for i in range(1,num+1):
#         if i == 1 or i == numero:
#             continue
#         if num % i == 0:
#             contador +=1
#     if contador == 0:
#         return True
#     else:
#         return False


def es_primo(num):
    p = True
    if num == 1:
        p = False
    for i in range(2,num):
        if num % i == 0:
            p = False
            break
    return p




def run():
    num = int(input('Escribe un numero: '))
    if es_primo(num):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == "__main__":
    run()
