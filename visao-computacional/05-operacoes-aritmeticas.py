import cv2 as cv

# 1) Adição de imagens

image1 = cv.imread('images/superman.png')
image2 = cv.imread('images/batman.png')

addedImage = cv.add(image1, image2)
#addedImage = image1 + image2 # Assim também é possível, porém não haverá tratamento dos pixels e pode resultar na distorção das cores

cv.imshow('Imagem somada', addedImage)

cv.waitKey(0)
cv.destroyAllWindows()


# 2) Subtração de imagens

image1 = cv.imread('images/superman.png')
image2 = cv.imread('images/batman.png')

subtractedImage = cv.subtract(image1, image2)
#subtractedImage = image1 - image2 # Assim também é possível, porém não haverá tratamento dos pixels e pode resultar na distorção das cores

cv.imshow('Imagem subtraída', subtractedImage)

cv.waitKey(0)
cv.destroyAllWindows()

# 3) Soma Ponderada

'''
A soma ponderada mescla, com perda de dados, duas imagens em apenas uma.

Método addWeighted(src1, alpha, src2, beta, gamma):

src1 = Matriz referente a primeira imagem
alpha = Peso (Itensidade) da primeira imagem
src1 = Matriz referente a segunda imagem
beta = Peso (Itensidade) da segunda imagem
gamma = Valor escalar adicionado a cada soma

OBS.: Os valores de alpha e beta variam de 0.1 a 1, sendo 0.1 equivalente a imagem transparente e 1 a intensidade máxima da imagem.

O gamma é utilizado para realizar ajustes na imagem.

Saída: Matriz da imagem mesclada
'''

image1 = cv.imread('images/superman.png')
image2 = cv.imread('images/batman.png')

mergedImage = cv.addWeighted(image1, 0.3, image2, 0.7, 0)

cv.imshow('Imagem Mesclada', mergedImage)

cv.waitKey(0)
cv.destroyAllWindows()