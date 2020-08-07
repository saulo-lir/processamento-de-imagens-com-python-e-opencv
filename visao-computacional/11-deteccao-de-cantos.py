import cv2 as cv
import numpy as np

# Preparação da imagem para ser feita a detecção dos cantos
image = cv.imread('images/hospital2.jpg')
imageGrey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
imageGrey = np.float32(imageGrey)

# Detecção dos cantos com a função cornerHarris(image, blockSize, ksize, k)

dst = cv.cornerHarris(imageGrey, 2, 3, 0.01)
element_estr = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
dst = cv.dilate(dst, element_estr)
image[dst > 0.05*dst.max()] = [255,0,0]

cv.imshow('Imagem com os cantos detectados', image)

cv.waitKey(0)
cv.destroyAllWindows()

# Detecção de cantos com melhor desempenho usando a função goodFeaturesToTrack(img, n, qual, k)

corners = cv.goodFeaturesToTrack(imageGrey, 10, 0.05, 0.25)

for item in corners:
    x,y = item[0]
    cv.circle(image, (x,y), 4, (255,0,0), -1)

cv.imshow('Imagem com os cantos detectados 2', image)

cv.waitKey(0)
cv.destroyAllWindows()