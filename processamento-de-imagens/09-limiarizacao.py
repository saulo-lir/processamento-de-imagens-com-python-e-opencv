import cv2

'''
A limiarização consiste em tornar a imagem binária, ou seja, com duas cores.
'''

image = cv2.imread('images/piscina-bolinhas.jpg')

# Mudar todos os pixeis da imagem para preto
for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        image[i][j] = (0,0,0)

# Escrever texto na imagem
fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, '255', (15,65), fonte, 2, (255,255,255),2)
cv2.putText(image, '70', (125,65), fonte, 2, (70,70,70),2)
cv2.putText(image, '100', (225,65), fonte, 2, (100,100,100),2)

# Esse texto será imperceptível, pois a cor (1,1,1) se aproxima muito de (0,0,0)
cv2.putText(image, '1', (405,65), fonte, 2, (1,1,1),2)

# Aplicando o inverso: Onde a cor for preta, será alterado para branco. Dessa forma o texto '1' ficará legível.
for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        if image[i][j][0] == 0:
            image[i][j] = (255,255,255)

# Deixando todos os valores legíveis. O background permanece preto, e tudo que não tiver a cor do background, ou seja, os textos nesse caso, as cores serão alteradas para branco.
for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        if image[i][j][0] != 0:
            image[i][j] = (255,255,255)

# Isolar apenas o elemento que possui um valor específico para exibí-lo.
for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        if image[i][j][0] == 1:
            image[i][j] = (255,255,255)
        else:
            image[i][j] = (0,0,0)

cv2.imshow('Imagem', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
