import cv2

image = cv2.imread('images/piscina-bolinhas.jpg')

# Intervalo de pixeis: Eixo y (coluna), Eixo x (linha)
imageCropped = image[100:200, 100:400] # Selecionando 100px de altura (200px - 100px) e 300px de largura (400px - 100px)

cv2.imshow('Imagem Original', image)
cv2.imshow('Imagem Cortada', imageCropped)

cv2.waitKey(0)