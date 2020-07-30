import cv2 as cv

# Sobrepor uma imagem na outra

backgroundImage = cv.imread('images/paisagem.jpg')
frontImage = cv.imread('images/samurai.png')

# 1) Cortar uma região da imagem maior com as mesmas medidas da imagem que será sobreposta

# Altura 0px até 324px, Largura 0px até 220px
crop = backgroundImage[0:324, 0:220]
# cv.imshow('Imagem cortada', crop)

# 2) Converter imagem frontal para cinza

frontImageGrey = cv.cvtColor(frontImage, cv.COLOR_BGR2GRAY)
# cv.imshow('Imagem em Cinza', frontImageGrey)

# 3) Aplicar a limiarização

ret, imageFrontBinarizada = cv.threshold(frontImageGrey, 100, 255, cv.THRESH_BINARY)
# cv.imshow('Imagem Binarizada', imageFrontBinarizada)

# 4) Aplicar operação binária para unir a imagem cortada com a imagem binarizada

fundo = cv.bitwise_and(crop, crop, mask = imageFrontBinarizada)
# cv.imshow('Imagem Alterada Fundo', fundo)

frontImageGreyInvertida = cv.bitwise_not(frontImageGrey)
# cv.imshow('Imagem em Cinza invertida', frontImageGreyInvertida)

frente = cv.bitwise_and(frontImage, frontImage, mask = frontImageGreyInvertida)
# cv.imshow('Imagem Alterada Frente', frente)

# 5) Juntar as imagens alteradas

imagemJunta = cv.add(frente, fundo)
# cv.imshow('Imagens alteradas unidas', imagemJunta)

# 6) Adicionar na imagem de background essa nova imagem que criamos. Devemos adicionar exatamente nos pixels correspondentes.

backgroundImage[0:324, 0:220] = imagemJunta
cv.imshow('Imagens Unidas', backgroundImage)

# OBS.: Caso não quisermos apenas sobrepor a imagem sem tratamento algum, basta executarmos o passo 6 com as imagens originais.

cv.waitKey(0)
cv.destroyAllWindows()