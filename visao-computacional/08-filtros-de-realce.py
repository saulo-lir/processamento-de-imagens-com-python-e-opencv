import cv2 as cv

# 1) Detector de Bordas - Sobel: Filtro espacial não linear usado para realçar bordas verticais e horizontais

image = cv.imread('images/predio.JPG')

# Aplica o filtro na vertical
sobelx = cv.Sobel(image, cv.CV_8U, 0, 1, ksize=7)

# Aplica o filtro na horizontal
sobely = cv.Sobel(image, cv.CV_8U, 1, 0, ksize=7)

cv.imshow('Filtro Sobel na vertical', sobelx)
cv.imshow('Filtro Sobel na horizontal', sobely)

cv.waitKey(0)
cv.destroyAllWindows()


# 2) Detector de Bordas - Laplaciano: Filtro espacial não linear que possui máscara de ordem 3

image = cv.imread('images/predio.JPG')

lap = cv.Laplacian(image, cv.CV_8U)
cv.imshow('Filtro Laplacian', lap)

cv.waitKey(0)
cv.destroyAllWindows()


# 3) Detector de Bordas - Canny: Baixa taxa de erro, Os pontos de borda devem estar bem localizaos, resposta de um único ponto de borda

image = cv.imread('images/predio.JPG')

canny = cv.Canny(image, 75, 50)
cv.imshow('Filtro Canny', canny)

cv.waitKey(0)
cv.destroyAllWindows()