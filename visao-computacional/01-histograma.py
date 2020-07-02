import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

'''
O Histograma de uma imagem é a distribuição da frequência dos níveis de cinza ou de uma cor em relação ao número de amostras. Essa distribuição nos fornece informações sobre a qualidade da imagem, principalmente no que diz respeito à intensidade luminosa e contraste.
'''

# 1) Exibir histograma de uma imagem cinza
image = cv.imread('images/cinza.jpg', 0) # 0 = Lê a imagem em nível de cinza, 1 = colorida, -1 = alfa

'''
FUNÇÃO HIST(img, Num1, Intervalo)
Entrada:

    1.Img = Imagem com a qual queremos trabalhar.
    2. Num1 = Número de elementos distintos que podem ser representados.
    3. Intervalo = Intervalo entre os elementos.

Saída: Gráfico representando o histograma da imagem

Função ravel

Função RAVEL(array)

Entrada:

    1. Img = Matriz de entrada, no caso a imagem. Os elementos em um são lidos na ordem especificada por ordem e empacotados como uma matriz 1-D.

Saída: retorna uma matriz plana contígua (matriz 1D com todos os elementos da matriz de entrada e com o mesmo tipo que ela).

Resumindo, a função ravel transforma a imagem em um vetor, organizando todo o elemento em uma estrutura.
'''

plt.hist(image.ravel(), 256, [0,256])
plt.show()

# 2) Uma imagem colorida possui histograma para cada canal de cor (R, G, B)
#  Exibir o histograma de uma imagem colorida

image = cv.imread('images/colorida.jpg')

# Separando os canais de cores da imagem com split

azul, verde, vermelho = cv.split(image)

# cv.imshow('Imagem', image)

figura = plt.figure(figsize=(20,5))

eixo1 = figura.add_subplot(131)
eixo1.hist(azul.ravel(), 256, [0,256])
plt.title('Histograma do canal azul')

eixo2 = figura.add_subplot(132)
eixo2.hist(verde.ravel(), 256, [0,256])
plt.title('Histograma do canal verde')

eixo2 = figura.add_subplot(133)
eixo2.hist(vermelho.ravel(), 256, [0,256])
plt.title('Histograma do canal vermelho')

plt.show()