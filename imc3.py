categorias = { "m": { 10 : [14.42, 19.60], 
                      11 : [14.83, 20.35],
                      12 : [15.24, 21.12],
                      13 : [15.74, 21.93],
                      14 : [16.18, 22.77],
                      15 : [16.59, 23.63],
                      16 : [17.01, 24.45],
                      17 : [17.31, 25.28],
                      18 : [17.54, 25.95],
                      19 : [17.80, 26.36],},

               "f": { 10 : [14.23, 20.19],
                      11 : [14.60, 21.18],
                      12 : [14.98, 22.17],
                      13 : [15.36, 23.08],
                      14 : [15.67, 23.88],
                      15 : [16.01, 24.29],
                      16 : [16.37, 24.74],
                      17 : [16.59, 25.23],
                      18 : [16.71, 25.56],
                      19 : [16.87, 25.85],},
            }

peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite sua altura em m: "))
idade = int(input("Digite sua idade: "))
sexo = input("Digite o seu sexo (m ou f): ")

imc = round(peso / (altura ** 2), 2)
print("Seu IMC é: ", imc)

if idade < 20:
    if imc < categorias[sexo][idade][0]: 
        print("Baixo Peso")

    elif imc < categorias[sexo][idade][1]:
        print("Adequado")

    else:
        print("Sobrepeso")

else:
    if imc < 18.5:
        print('Abaixo do peso')
    elif imc < 25:
        print('Peso normal')
    elif imc < 30:
        print('Pré obesidade')
    elif imc < 35:
        print('Obesidade grau 1')
    elif imc < 40:
        print('Obesidade grau 2')
    else:
        print('Obesidade grau 3')
