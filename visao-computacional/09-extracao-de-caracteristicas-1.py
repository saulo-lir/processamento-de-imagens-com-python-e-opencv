import cv2 as cv
import numpy as np

'''
Objetivo: Obter informações que tornam possível classificar ou identificar um objeto

Categorias:
- Aspectos
- Dimensionais
- Inerciais
- Topológicas
'''

# 1) Aspectos: Define informações sobre a sua cor. Valores estatísticos das cores da imagem: Média e desvio padrão.

image_color = cv.imread('images/tampa_azul.jpg', 1) # Ler em imagem em colorido
image_grey = cv.imread('images/tampa_azul.jpg', 0) # Ler imagem em escala de cinza

'''
A função mean retorna a média de todos os canais RGB começando pelo azul, depois o verde e por último o vermelho. O quarto parâmetro é o valor do alpha da imagem. Pode-se dizer que seria a transparencia da imagem.

A função meanStdDev calcula a média e o desvio padrão da imagem de forma independente para cada canal e os retorna através dos parâmetros de saída.

Assim, os valores mean e stdev são valores escalares para as imagens coloridas que dividem a imagem em canais e calculam e aplicam um limite para cada canal de forma independente.

Para essa programação é usada também a função flatten. Essa função retorna uma cópia da matriz em uma dimensão 1D.
'''

valorMedio = cv.mean(image_color)
valorMedioGrey = cv.mean(image_grey)

(meanColor, stdColor) = cv.meanStdDev(image_color)
(meanGrey, stdGrey) = cv.meanStdDev(image_grey)

RGB = np.concatenate([meanColor, stdColor]).flatten()
Grey = np.concatenate([meanGrey, stdGrey]).flatten()

print('Valores da média e desvio padrão RGB')
print(valorMedio)
print(RGB)

print('Valores da média e desvio padrão em tons de cinza')
print(valorMedioGrey)
print(Grey)


# 2) Dimensionais: Refere-se ao tamanho do objeto: Área, Perímetro e Diâmetro.

image = cv.imread('images/triangle.JPG', 0)

# Binarizar a imagem

_, imgBin = cv.threshold(image, 0, 255, cv.THRESH_BINARY_INV)

'''
A área de um objeto de interesse é definida pelo total de pixeis que o representa. E através da função cotourArea é possível obte-la.

Para o uso dessa função é preciso primeiro usar outra função, a findContours. Essa função extrai de uma imagem binária os pontos que representam os contornos dos objetos segmentados.
'''

modo = cv.RETR_TREE
metodo = cv.CHAIN_APPROX_SIMPLE

_, contorno, hierarquia = cv.findContours(imgBin, modo, metodo)

if len(contorno) > 0:
    obj = contorno[0]
    area = cv.contourArea(obj)
    print(area)

    perimetro = cv.arcLength(obj, True)
    print(perimetro)
else:
    print('Sem contorno encontrado')