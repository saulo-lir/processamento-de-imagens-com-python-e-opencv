import cv2 as cv

'''
Filtros de suavização

Filtros Lineares:
    -> Passa-baixas
    -> Passa-altas

Filtros não lineares
'''

# 1) Filtro de Média (Linear passa-baixa): Substitui cada pixel da imagem pelo valor médio de sua vizinhança

image = cv.imread('images/einstein-2.png')
imageFiltrada = cv.blur(image, (5,5))

cv.imshow('Imagem Filtrada', imageFiltrada)

cv.waitKey(0)
cv.destroyAllWindows()


# 2) Filtro Gaussiano (Linear passa-baixa): Excelentes resultados para tratamento de ruídos gaussianos

image = cv.imread('images/formas.PNG')
imageFiltrada = cv.GaussianBlur(image, (5,5), 0)

cv.imshow('Imagem Filtrada', imageFiltrada)

cv.waitKey(0)
cv.destroyAllWindows()

# 3) Filtro Mediano (Não Linear passa-baixa): Excelentes resultados para tratamento de ruídos do tipo sal e pimenta

image = cv.imread('images/head.PNG')
imageFiltrada = cv.medianBlur(image, 5, 0)

cv.imshow('Imagem Filtrada', imageFiltrada)

cv.waitKey(0)
cv.destroyAllWindows()