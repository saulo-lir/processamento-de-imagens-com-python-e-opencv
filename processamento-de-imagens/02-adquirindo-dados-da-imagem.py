import cv2

image = cv2.imread('images/piscina-bolinhas.jpg')

# 1) Exibir a altura da imagem em pixel
print(image.shape[0])

# 2) Exibir a largura da imagem em pixel
print(image.shape[1])

# 3) Exibir a quantidade de canais de cores da imagem
print(image.shape[2])

# 4) Exibir todas as listas com o valor de cada pixel da imagem (usar apenas o print(image) imprime de forma resumida)
for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        print(image[i][j])

# 5) Exibir canal por canal de cada pixel
for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        for h in range(0, 3): # 3 é a quantidade de canais da imagem. Pra essa imagem, poderia ser também: range(0, image.shape[2])
            print(image[i][j][h])