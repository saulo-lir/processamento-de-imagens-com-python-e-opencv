import cv2

image = cv2.imread('images/piscina-bolinhas.jpg')

'''
O split serve para dividir a imagem em cada um dos 3 canais BGR.
Então por exemplo, para o primeiro canal, o azul, todos os pixeis que tiverem o valor 255, que seria o azul total, serão exibidas em branco.

Para os valores abaixo disso, a imagem será exibida em escala de cinza.

Quando for 0, a imagem ficará preta.

O mesmo se aplica para os demais canais.

Resumindo, o split serve para exibir a imagem com cada canal de forma individual, em escala de cinza.

'''

# Blue (B=255, G=0, R=0), (B=0, G=255, R=0), Red (B=0, G=0, R=255)
(b, g, r) = cv2.split(image)

cv2.imshow('Imagem Original', image)
cv2.imshow('Imagem no Canal Azul', b)
cv2.imshow('Imagem no Canal Verde', g)
cv2.imshow('Imagem no Canal Vermelho', r)

# Juntando a imagem separada
imageMerged = cv2.merge((b, g, r))
cv2.imshow('Imagem Original 2', imageMerged)

cv2.waitKey(0)
cv2.destroyAllWindows()