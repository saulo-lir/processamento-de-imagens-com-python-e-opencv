import cv2

image = cv2.imread('images/piscina-bolinhas.jpg')

# 1) Exibir os valores RGB do primeiro pixel da imagem:

    # Eixo y (coluna), Eixo x (linha)
print(image[0][0])

# 2) Alterando o valor do primeiro pixel para branco:
image[0][0] = (255,255,255)

# 3) Alterando o valor de um intervalo de pixeis para branco:
image[0:10,0:10] = (255,255,255)

# 4) Alterando a cor da linha do topo da imagem para branco. A coluna vai de 0 a 10, enquanto que a linha de 0 até o último ponto.
image[0:10, :] = (255,255,255)


# 5) Alterando a cor dinamicamente
branco = (255,255,255)

# Mudando a cor de todos os pixeis da imagem para branco
for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        image[i][j] = branco

# Mudando a cor de 10 em 10 pixels para branco
for i in range(0, image.shape[0], 10):
    for j in range(0, image.shape[1], 10):
        image[i][j] = branco

# Mudando a cor do pixel quando o canal B (azul) for 255. (Lembrando que para o pixel ser azul, a lista deve ser [255, 0, 0])
for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        if image[i][j][0] == 255:
            image[i][j] = branco

cv2.imshow('Imagem', image)
cv2.waitKey(0)