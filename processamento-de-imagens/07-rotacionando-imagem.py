import cv2

image = cv2.imread('images/piscina-bolinhas.jpg')

# 1) Rotacionando no eixo x (da esquerda pra direita)
imagemRotacionada = image[:, ::-1]

# 2) Rotacionando no eixo y (de cima para baixo)
imagemRotacionada = image[::-1, :]

# 2) Rotacionando tanto no eixo x quanto no y (da esquerda pra direita + de cima para baixo)
imagemRotacionada = image[::-1, ::-1]

cv2.imshow('Imagem Original', image)
cv2.imshow('Imagem Rotacionada', imagemRotacionada)
cv2.waitKey(0)