import cv2 as cv
import numpy as np

# 1) Rotação

'''
Argumentos do método getRotationMatrix2D:

Centro = Centro da imagem (total de colunas/2 e total de linhas/2)
Ângulo = Ângulo que deseja rotacionar a imagem
Escala = Fator de escala (default = 1)

Saída: Retorna uma matriz de rotação que será utilizada no próximo método

Argumentos do método warpAffine:

Src = Matriz referente a imagem original
Matriz = Matriz de rotação
Dsize = Tamanho da imagem rotacionada

Saída: Imagem rotacioanda
'''

image = cv.imread('images/piramide.jpg', 0)

totalLinhas, totalColunas = image.shape

rotationMatrix = cv.getRotationMatrix2D((totalLinhas/2, totalColunas/2), 90, 1)
imagemRotacionada = cv.warpAffine(image, rotationMatrix, (totalColunas, totalLinhas))

cv.imshow('Imagem Original', image)
cv.imshow('Imagem Rotacionada', imagemRotacionada)

cv.waitKey(0)
cv.destroyAllWindows()


# 2) Translação (Deslocar a imagem em relação a sua posição inicial)

'''
Para deslocarmos uma imagem, utilizamos o mesmo método warpAffine, porém precisamos
fornecer uma matriz de translação, obtidada através do método float32 da biblioteca numpy

Argumentos do método float32:
[h,v,px] = horizontal, vertical, quantidade de pixel referente ao deslocamento.

Saída: Nova imagem deslocada
'''

image = cv.imread('images/einstein.jpg', 0)

totalLinhas, totalColunas = image.shape
                    # Deslocamento horizontal, # Deslocamento vertical
translationMatrix = np.float32([[1,0,100], [1,0,100]])
imagemDeslocada = cv.warpAffine(image, translationMatrix, (totalColunas, totalLinhas))

cv.imshow('Imagem Deslocada', imagemDeslocada)

cv.waitKey(0)
cv.destroyAllWindows()


# 3) Ajuste de escala

'''
Argumentos do método resize:

src = Matriz referente a imagem
dst = Imagem de saída
fx = Fator de escala horizontal
fy = Fator de escala vertical
interpolation = Método de interpolação

Saída: Imagem modificada
'''

image = cv.imread('images/einstein.jpg', 0)

imagemModificada = cv.resize(image, None, fx = 0.8, fy = 0.8, interpolation = cv.INTER_CUBIC)

cv.imshow('Imagem Original', image)
cv.imshow('Imagem Modificada', imagemModificada)

cv.waitKey(0)
cv.destroyAllWindows()


# 3) Alterar Perspectiva

image = cv.imread('images/papelAlterado.png', 0)

# Pegar as coordenadas dos 4 cantos da imagem original
coordenates_1 = np.float32([[195,9], [421,126], [49,372], [319,470]])

# Colocar as coordenadas desejadas para transformação
coordenates_2 = np.float32([[0,0], [430,0], [0,564], [430,564]])

# OBS.: Para pegar as coordenadas dos pixels, é necessário utilizar alguma ferramenta específica para isso ou o próprio python

transformationMatrix = cv.getPerspectiveTransform(coordenates_1, coordenates_2)
imagemModificada = cv.warpPerspective(image, transformationMatrix, (430,564))

cv.imshow('Imagem Original', image)
cv.imshow('Imagem Transformada', imagemModificada)

cv.waitKey(0)
cv.destroyAllWindows()