import cv2 as cv

# 3) Inerciais e Hu: Momentos de uma imagem (momentos estatísticos), Centro geométrico, Formas geométricas. Objetos que tenham sofrido alterações em: Escala, Rotação, Translação.

'''
As características inerciais definem informações sobre os momentos, o centro geométrico e as formas geométricas envolventes de um objeto de interesse.

É possível através dessas características reconhecer objetos mesmo que tenham sofrido alterações na escala, rotação ou translação.

Os momentos de uma imagem, também conhecidos como momentos estatísticos, é um dos métodos principais para extração de características. São obtidos por funções matemáticas, com base estatisticas, que fornecem valores que representam um determinado objeto.

Através de imagens binárias, podemos calcular esses momentos. A função moments extrai essas características retornando 24 momentos que caracterizam a imagem.

Pode-se usar esses momentos para calcular por exemplo, a área, médias e centróide de um objeto.
'''

image = cv.imread('images/circle.JPG', 0)

momentos = cv.moments(image)

print(len(momentos))
print(momentos)
print('\n')

# Área da imagem
area = momentos['m00']

print('Área')
print(area)
print('\n')

# Médias da imagem
areax = momentos['m10'] / area
areay = momentos['m01'] / area

print('Médias')
print(areax)
print(areay)
print('\n')

# Centróide
centroidex = int(momentos['m10'] / momentos['m00'])
centroidey = int(momentos['m01'] / momentos['m00'])

print('Centróide')
print(centroidex)
print(centroidey)
print('\n')


# Momentos invariantes em Hu (7 momentos)

'''
Os momentos invariantes de Hu são 7 momentos calculados a partir dos momentos de uma imagem. Através deles, podemos obter a área, centro geométrico e até mesmo um vetor de características invariantes em escala, rotação e translação de um objeto.

A função HuMoments calcula esses momentos invariantes. Essa função requer como parâmetro apenas os momentos do objeto.
'''

# Retorna os 7 melhores momentos encontrados
momentosHu = cv.HuMoments(momentos)
print(momentosHu.flatten())
