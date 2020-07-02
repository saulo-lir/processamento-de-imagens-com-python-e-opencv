import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

'''
O objetivo da equalização de imagens é a melhoria do seu contraste.

Para tanto, o ideal é que os níveis de cinza sejam representados de maneira uniforme e distribuída

A equalização de histograma consiste na redistribuição dos valores de nível de cinza em uma imagem, de forma que todos os pixels tenham a probabilidade de aparecer mais equalitária possível.
'''

image = cv.imread('images/einstein.jpg', 0)

# Equalizar o histograma
imgEqualizada = cv.equalizeHist(image)

cv.imshow('Imagem Original', image)
cv.imshow('Imagem Equalizada', imgEqualizada)


# Exibir os histogramas original e equalizado
plt.hist(image.ravel(),256,[0,256])
plt.show()

plt.hist(imgEqualizada.ravel(),256,[0,256])
plt.show()

cv.imwrite('images/einsteinEqualizado.jpg', imgEqualizada)

cv.waitKey()
cv.destroyAllWindows()

