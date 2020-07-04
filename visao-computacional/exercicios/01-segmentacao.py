'''
Utilizando o método de limiarização de OTSU, limiarize a digital (digital.png) de forma binária para facilitar a identificação do objeto.
'''

import cv2
import matplotlib.pyplot as plt

image = cv2.imread('digital.png', 0)

method = cv2.THRESH_BINARY + cv2.THRESH_OTSU

ret, imageOtsu = cv2.threshold(image, 0, 255, method)

cv2.imshow('Imagem Original', image)
cv2.imshow('Imagem Binarizada por OTSU', imageOtsu)

cv2.imwrite('digitalBinarizadaPorOTSU.png', imageOtsu)

cv2.waitKey()
cv2.destroyAllWindows()

