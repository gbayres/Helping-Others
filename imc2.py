'''
Não sei se você conhece a estrutura de dicionários, mas eu a usaria
pra o seu propósito. Pra exemplificar a sintaxe do dicionário,
eu poderia ter um dicionário que relaciona termos aos seus respectivos
significados, como por exemplo:

significados = {"guitarra": "Um instrumento musical"}

Se eu pedisse um print de significados["guitarra"], a saída seria
"Um instrumento musical". "guitarra" é uma chave e "Um instrumento musical"
é o valor dessa chave.

Qualquer coisa pode ser o valor de uma chave, inclusive outro dicionário.
Por exemplo, vamos supor que eu quero descobrir o nome dos professores de um
curso na faculdade...  

cursos = {"medicina":    {"Infectologia": "Patrícia",
                          "Pediatria"   : "Williane"},

          "engenharia":  {"Cálculo"       : "Rodrigo",
                          "Álgebra Linear": "Bruno"} 

Se eu solicitasse cursos["medicina"]["Pediatria"], descobriria que a professora
desse curso se chama "Williane".
E é isso que eu vou usar...

Farei um dicionário chamado categorias que tem 2 chaves relativas aos
sexos: "m" e "f"...
Cada uma dessas chaves terão um outro dicionário como valor.
As chaves desse outro dicionário representam a idade e os valores
representam os intervalos dos pesos.

Na tabela abaixo, uma pessoa de sexo "m" e idade = 10, teria as faixas de
peso "< 13.7", "13.7 - 18.5", "18.5 - 21.6" e "> 21.6", por exemplo.


'''


categorias = { "m": { 10 : [21.6, 18.5, 13.7], 
                      11 : [22.0, 19.3, 14.2],
                      12 : [23.0, 20.0, 14.6],
                      13 : [24.2, 21.0, 15.0],
                      14 : [25.3, 21.9, 15.6],
                      15 : [26.4, 22.8, 16.2],
                      16 : [27.3, 23.7, 16.7],
                      17 : [28.0, 24.5, 17.2],
                      18 : [28.6, 25.0, 17.5],
                      19 : [30.0, 25.0, 18.5],},

               "f": { 10 : [22.0, 19.1, 13.6],
                      11 : [23.2, 20.0, 14.0],
                      12 : [24.4, 20.9, 14.5],
                      13 : [25.6, 22.0, 15.1],
                      14 : [26.6, 22.9, 15.6],
                      15 : [27.6, 23.6, 16.1],
                      16 : [28.3, 24.3, 16.4],
                      17 : [28.6, 24.6, 16.6],
                      18 : [28.9, 24.9, 16.7],
                      19 : [30.0, 24.9, 18.5],},
            }

peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite sua altura em m: "))
idade = int(input("Digite sua idade: "))
sexo = input("Digite o seu sexo (m ou f): ")

imc = round(peso / (altura ** 2), 2) #Calcula o IMC e arredonda com 2 casas depois da vírgula
print("Seu IMC é: ", imc)

# Se o imc for maior que o referido pela categoria, o if para e imprime "obesidade" 
# Se não for, vai pro próximo item

if imc > categorias[sexo][idade][0]: 
    print("Obesidade")

# Se o imc for maior que o referido pela categoria, o if para e imprime "pré-obesidade" 
# Se não for, vai pro próximo item

elif imc > categorias[sexo][idade][1]:
    print("Pré-obesidade")

# Se o imc for maior que o referido pela categoria, o if para e imprime "Peso normal" 
# Se não for, vai pro próximo item

elif imc > categorias[sexo][idade][2]:
    print("Peso normal")

# Se não for nenhum dos anteriores, imprime "Abaixo do peso"
else:
    print("Abaixo do peso")
