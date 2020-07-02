import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

'''
Segmentar consiste em isolar e separar uma determinada região da imagem para posterior análise.
A limiarização de uma imagem é uma técnica usada para aplicar a segmentação.
'''

# Limiarização Binária (Binarização)

image = cv.imread('images/cafe.jpg')

metodo = cv.THRESH_BINARY_INV # O objeto de interesse ficará na cor branca

# O método threshold retorna 2 valores: Limite usado no limiar e a imagem limiarizada

ret, imagemBinarizada = cv.threshold(image, 200, 255, metodo)

cv.imshow('Imagem original', image)
cv.imshow('Imagem com limiarização binária', imagemBinarizada)
cv.imwrite('images/cafeBinarizado.jpg', imagemBinarizada)

cv.waitKey()
cv.destroyAllWindows()


# Binarização Adaptativa

image = cv.imread('images/olho.PNG', 0)

imgGauss = cv.medianBlur(image, 7)

th2 = cv.adaptiveThreshold(imgGauss, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 5)
th3 = cv.adaptiveThreshold(imgGauss, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow('Imagem Original', image)
cv.imshow('Imagem Média', th2)
cv.imshow('Imagem Gaussiana', th3)

cv.imwrite('images/olhoBinarizadoAdptativoMean.jpg', th2)
cv.imwrite('images/olhoBinarizadoAdaptativoGaussian.jpg', th3)

cv.waitKey()
cv.destroyAllWindows()


# Binarização por OTSU

image = cv.imread('images/cafe.jpg', 0)

metodo = cv.THRESH_BINARY_INV + cv.THRESH_OTSU

ret, imagemBinaria = cv.threshold(image, 0, 255, metodo)

print('O melhor limiar é: ', ret)

plt.hist(image.ravel(), 256, [0,256])
cv.imshow('Imagem Original', image)
plt.show()
cv.imshow('Imagem Binarizada por OTSU', imagemBinaria)

cv.imwrite('images/cafeBinarizadoPorOTSU.jpg', imagemBinaria)

cv.waitKey()
cv.destroyAllWindows()