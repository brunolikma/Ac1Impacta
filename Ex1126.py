diaDaSemanaqueComprou = input()
diasParaEntrega = int(input())
listDiaDaSemana = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
posicaoDodiaDasemana = listDiaDaSemana.index(diaDaSemanaqueComprou)
i = 0
if (diasParaEntrega == 0):
    print("chega hoje!")
else:
    while i <= diasParaEntrega:
        if (posicaoDodiaDasemana > len(listDiaDaSemana) -1 ):
            posicaoDodiaDasemana = 0

        posicaoDodiaDasemana += 1
        i += 1

    print("sera entregue " + listDiaDaSemana[posicaoDodiaDasemana - 1])