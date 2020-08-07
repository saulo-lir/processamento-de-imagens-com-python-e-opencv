import cv2 as cv
import numpy as np

'''
Template Matching (Correspondência de modelos): Técnica usada para classificação de objetos comparando porções das imagens uma com as outras.

Se o desvio padrão da imagem do modelo comparado à imagem de origem for pequeno o suficiente, a correspondência de modelo poderá ser usada.

É o método utilizado para localizar o local de uma imagem de modelo em uma imagem maior. O OpenCV vem com a função cv2.matchTemplate() para essa finalidade. Ela simplesmente desliza a imagem do modelo sobre a imagem de entrada (como na covolução 2D) e compara o modelo e o patch da imagem de entrada sob a imagem do modelo. O retorno da função é uma imagem em escala de cinza, em que cada pixel indica o quanto a vizinhança desse pixel corresponde ao modelo.
'''

# Converter BGR em RGB

full = cv.imread('images/ex_template_matching.jpg')
full = cv.cvtColor(full, cv.COLOR_BGR2RGB)

face = cv.imread('images/rosto_template.JPG')
face = cv.cvtColor(face, cv.COLOR_BGR2RGB)

# Vamos utilizar a função eval() = Converte string em função. Iremos utilizar várias strings que correspondem a métodos usados pelo matchTemplate() que fazem a correlação. Dessa forma, conseguimos ver qual é a melhor.

# Preparação para utilizar o método matchTemplate()

# Altura, largura e canal do template matching
height, width, channels = face.shape

# Todos os 6 métodos para comparação em uma lista
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

# Aplicando os métodos num for

for m in methods:

    # Criar uma cópia da imagem
    full_copy = full.copy()

    # Usar a função eval passando as strings
    method = eval(m)

    # Aplicar o template matching com os métodos
    result = cv.matchTemplate(full_copy, face, method)

    #cv.imshow(m, result)

# cv.waitKey(0)
# cv.destroyAllWindows()


# Verificar onde está o template matching

for m in methods:

    # Criar uma cópia da imagem
    full_copy = full.copy()

    # Usar a função eval passando as strings
    method = eval(m)

    # Aplicar o template matching com os métodos
    result = cv.matchTemplate(full_copy, face, method)

    # Pegar os valores Max e Min, além de seus locais
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    # Configurar o retângulo a ser desenhado em volta da área encontrada
    # Se o método for TM_SQDIFF ou TM_SQDIFF_NORMED, pegar o min
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + width, top_left[1] + height)

    # Desenhando o retângulo na área identificada
    cv.rectangle(full_copy, top_left, bottom_right, 255, 10)

    cv.imshow(m, result)
    cv.imshow(m, full_copy)

cv.waitKey(0)
cv.destroyAllWindows()