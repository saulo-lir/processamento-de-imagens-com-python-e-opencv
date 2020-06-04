import cv2

'''
Também conhecida com blur, consiste na distorção / borrão da imagem.

Essa técnica é útil para auxiliar na identificação de objetos.
'''

image = cv2.imread('images/piscina-bolinhas.jpg')

# 1) Criar pontos brancos na imagem

for i in range(0, image.shape[0], 15):
    for j in range(0, image.shape[1], 15):
        image[i:i+3, j:j+3] = (255,255,255)


# 2) Aplicar a suavização
                    # Tamanho da suavização
suave = cv2.blur(image, (5,5))

cv2.imshow('Imagem', suave)
cv2.waitKey(0)
cv2.destroyAllWindows()