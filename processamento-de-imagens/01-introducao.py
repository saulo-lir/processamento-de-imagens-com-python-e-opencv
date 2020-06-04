import cv2

'''
- Uma imagem colorida é formada por 3 canais de cores: Red, Green, Blue (RGB)
- Cada canal possui de 0 a 255 valores

- Ex.: Uma imagem que possui os canais: [255, 0, 0], terá a cor vermelha,
pois 255 na primeira posição equivale a cor máxima do vermelho, enquanto que
0 nas outras posições indica o valor nulo das suas respectivas cores.

- Cada pixel de uma imagem contém uma lista com os 3 canais RGB.
- Uma imagem é composta por uma matriz tridimensional. É como se tivéssemos uma
matriz em cima de outra matriz 3 vezes.

-- Na biblioteca Open CV, ao invés de ser usado o padrão RGB, é usado o BGR. Então,
na lista [255, 255, 255], temos Azul, Verde e Vermelho (que juntando fica branco).
'''

# Lendo uma imagem e transformando ela numa matriz tridimensional
image = cv2.imread('images/piscina-bolinhas.jpg')
print(image)

# Exibindo a imagem lida:

# Nome da janela, variável que contém os píxeis da imagem
cv2.imshow('Exibindo Imagem', image)

# Permite que a janela com a imagem fique aberta até pressionarmos qualquer tecla
cv2.waitKey(0)