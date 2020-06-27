import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
O histograma serve para exibir um gráfico com a frequência com que um determinado valor aparece para cada cor da imagem.

Ex.: O valor 127 aparece 5 vezes na camada vermelha.
     O valor 70 aparece 2 vezes na camada verde.
'''

image = cv2.imread('images/piscina-bolinhas.jpg')

# 1) Separar os canais de cores sem usar o split(). (Pode ser feito com split, mas para vermos a lógica, vamos fazer na raça)

listaAzul = []
listaVerde = []
listaVermelho = []

totalListaAzul = []
totalListaVerde = []
totalListaVermelho = []

for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        listaAzul.append(image[i][j][0])
        listaVerde.append(image[i][j][1])
        listaVermelho.append(image[i][j][2])

#print(listaAzul)

# 2) Separar em outra lista todos valores da lista original, sem repetição
listaAzulSemNumerosRepetidos = sorted(set(listaAzul))
#print(listaAzulSemNumerosRepetidos)

# 3) Fazer a contagem do número de vezes que cada número aparece na lista original
# Canal Azul
for i in range(0, len(listaAzulSemNumerosRepetidos)):
    total = 0

    for j in range(0, len(listaAzul)):
        if listaAzulSemNumerosRepetidos[i] == listaAzul[j]:
            total += 1

    totalListaAzul.append(total)

#print(totalListaAzul)

# Canal Verde
listaVerdeSemNumerosRepetidos = sorted(set(listaVerde))

for i in range(0, len(listaVerdeSemNumerosRepetidos)):
    total = 0

    for j in range(0, len(listaVerde)):
        if listaVerdeSemNumerosRepetidos[i] == listaVerde[j]:
            total += 1

    totalListaVerde.append(total)

#print(totalListaVerde)

# Canal Vermelho
listaVermelhoSemNumerosRepetidos = sorted(set(listaVermelho))

for i in range(0, len(listaVermelhoSemNumerosRepetidos)):
    total = 0

    for j in range(0, len(listaVermelho)):
        if listaVermelhoSemNumerosRepetidos[i] == listaVermelho[j]:
            total += 1

    totalListaVermelho.append(total)

#print(totalListaVermelho)

# 4) Exibir o histograma

    # Lista de valores, cor da linha do gráfico
plt.plot(totalListaVermelho, color='red')
plt.plot(totalListaVerde, color='green')
plt.plot(totalListaAzul, color='blue')

plt.show()

'''
Outra forma de calcular e exibir os histogramas: Utilizando a função calcHist() e loop.
(Método utilizado nas aulas de computação gráfica do IFAL)
'''

image = cv2.imread('images/piscina-bolinhas.jpg')
color = ('b', 'g', 'r')

for key,value in enumerate(color):
    histograma = cv2.calcHist([image], [key], None, [256], [0,256])
    plt.plot(histograma, color=value)
    plt.xlim([0,256])

plt.savefig('images/histogramaColorido.jpg')
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()