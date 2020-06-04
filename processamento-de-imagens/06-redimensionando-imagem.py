import cv2

image = cv2.imread('images/piscina-bolinhas.jpg')

# 1) Redimensionando com valores fixos (Pode não manter a proporção a imagem)
larguraNova = 100
alturaNova = 100

image = cv2.resize(image, (larguraNova, alturaNova))

# 2) Redimensionando a imagem baseado na largura e altura dela (Não distorce a imagem. Matém sua proporção)
largura = image.shape[1]
altura = image.shape[0]
proporcao = float(altura/largura)

larguraNova = 150
alturaNova = int(larguraNova * proporcao) # Tanto faz aplicar o valor dinâmico na altura ou largura

image = cv2.resize(image, (larguraNova, alturaNova))

cv2.imshow('Imagem', image)
cv2.waitKey(0)