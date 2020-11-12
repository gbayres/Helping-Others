
##registro = [("joao", 2), ("joaquim", 4), ("farias", 1), ("geferson", 3), ("bauducco", 7), ("teresa", 4), ("luiz", 3)]
##ord_por_nota = registro[:]
##ord_por_nome = registro[:]

registro = []


nota = 0
while nota >= 0:
    print("\n=== Nova entrada ===\n")
    nome = input("Insira o nome do aluno: ")
    nota = round(float(input("Insira a nota do aluno: ")), 1)

    if nota >= 0:
        registro.append([nome, nota])

    if nota < 0 and len(registro) == 0:
        print("\nVocê deve ter ao menos um aluno registrado! ")
        nota = 0
    
   
    
ord_por_nota = registro[:]
ord_por_nome = registro[:]

seleção = 0;
while seleção != '6':

    print('''
======================
1 - Estatísticas
2 - Notas por faixa
3 - Busca por nome
4 - Frequências
5 - Incluir novo aluno
6 - Finalizar
======================
''')
            
    seleção = input("Selecione uma opção: ")
    print()
    
    #=====================ORDENANDO O REGISTRO=====================

    #---------Por valor-----------
    if len(registro) > 1:

        continuar = True

        while continuar:
            continuar = False
            for i in range(len(registro) - 1):
                if ord_por_nota[i][1] > ord_por_nota[i + 1][1]:

                    ord_por_nota[i], ord_por_nota[i + 1] =\
                    ord_por_nota[i + 1], ord_por_nota[i]

                    continuar = True

    #--------Por nome------------
        continuar = True

        while continuar:
            continuar = False
            for i in range(len(registro) - 1):

                #Perceba que o método sorted será aplicado a uma tupla, não a uma lista
                
                if sorted((ord_por_nome[i][0], ord_por_nome[i + 1][0])) ==\
                   [ord_por_nome[i + 1][0], ord_por_nome[i][0]]:

                    ord_por_nome[i], ord_por_nome[i + 1] =\
                    ord_por_nome[i + 1], ord_por_nome[i]

                    continuar = True

    #==============================================================

    if seleção == '1':

        #==============CALCULAR MAIOR FREQUENCIA======================
        #------Calcular frequencias
        notas = [aluno[1] for aluno in registro]
        notas_unicas = list(set(notas))
        frequencias = [0 for i in range(len(notas_unicas))]

        for i in range(len(notas_unicas)):
            for nota in notas:
                if nota == notas_unicas[i]:
                       frequencias[i] += 1

        freq_de_notas = list(zip(notas_unicas, frequencias))

        #-----Definir maiorr frequencia
        maior = 0
        for itens in freq_de_notas:
            if itens[1] > maior:
                maior = itens[1]

        #=============CALCULAR MÉDIA=================================
        soma = 0
        for nota in registro:
            soma += nota[1]

        media = round( soma / len(registro), 2)

        #==============CALCULAR MEDIANA===============================
        posição_meio = int(len(registro) / 2 + 0.5)

        if len(registro) % 2 == 1:
            mediana = ord_por_nota[posição_meio - 1][1]
        else:
            mediana = (ord_por_nota[posição_meio - 1][1] + ord_por_nota[posição_meio][1]) / 2

        mediana = round(mediana, 2)

        #==============CALCULAR DESVIO PADRÃO=========================

        dp = 0

        for nota in registro:
            dp += (nota[1] - media) ** 2

        if len(registro) > 1:
            dp = dp / len(registro) - 1
            dp = dp ** (1/2)

        else:
            dp = 0

        dp = round(dp, 2)
            
        print(f'Nota máxima: {ord_por_nota[-1][1]}')
        print(f'Nota mínima: {ord_por_nota[0][1]}')
        print(f'Média: {media}')
        print(f'Primeira Moda: ')
        for itens in freq_de_notas:
            if itens[1] == maior:
                print(f'\tNota: {itens[0]} | Frequência: {itens[1]}')
        print(f'Mediana: {mediana}')
        print(f'Desvio Padrão: {dp}')
        print()
                
                

    elif seleção == '2':
        
        minimo = round(float(input("Defina uma nota mínima: ")), 1)
        maximo = round(float(input("Defina uma nota máxima: ")), 1)
        print()

        for aluno in ord_por_nome:
            if minimo <= aluno[1] <= maximo:
                print(f"Aluno: {aluno[0]} | Nota: {aluno[1]}")


    elif seleção == '3':

        string = input("Insira a string que o nome deve conter: ")
        print()
        
        for item in ord_por_nome:
            if string in item[0]:
                print(f"Aluno: {item[0]} | Nota: {item[1]}")

        
    elif seleção == '4':

        #==============CALCULAR FREQUENCIAS======================
        notas = [aluno[1] for aluno in registro]
        notas_unicas = list(set(notas))
        frequencias = [0 for i in range(len(notas_unicas))]

        for i in range(len(notas_unicas)):
            for nota in notas:
                if nota == notas_unicas[i]:
                       frequencias[i] += 1

        freq_de_notas = list(zip(notas_unicas, frequencias))

        #=======================================================
        minimo = round(float(input("Defina uma nota mínima: ")), 1)
        maximo = round(float(input("Defina uma nota máxima: ")), 1)
        print()
        
        for nota in freq_de_notas:
            if minimo <= nota[0] <= maximo:
                print(f"Nota: {nota[0]} | Frequência: {nota[1]}")
                       
        
    elif seleção == '5':
        print("\n=== Nova entrada ===\n")
        nome = input("Insira o nome do aluno: ")
        nota = round(float(input("Insira a nota do aluno: ")), 1)
        registro.append((nome, nota))

        ord_por_nota = registro[:]
        ord_por_nome = registro[:]

    elif seleção == '6':
        print("Terminando programa...")

    else:
        print("Valor inválido")


    input("Aperte Enter para continuar")
