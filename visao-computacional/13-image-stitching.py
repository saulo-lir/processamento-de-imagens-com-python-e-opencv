import cv2 as cv
import numpy as np

'''
Captação de várias imagens de uma cena e organiza-las em uma única cena maior.
Tais fotos das cenas ordenadas são chamadas de panoramas.
Todo o processo de aquisição de várias imagens e conversão em panoramas é chamado de image stitching.

Etapas:

1- Calcular os key-points e os descritores desses key-points na imagem;

-> Consiste na identificação de características: Feature Detection
Essas características podem ser obtidas através dos seguintes algoritmos:
    - Haris Corner Detection
    - Shi-Tomasi Corner Detection
    - SIFT (Scale-Invariant Feature Trasform)
    - SURF (Speeded-Up Robust Features)
    - FAST algorithm for corner detection
    - BRIEF (Binary Robust Independent Elementary Features)
    - ORB (Oriented FAST and Rotated Brief) (Não patenteado - livre para uso, combina ambos FAST e BRIEF)


2- Calcular as distâncias entre todos os descritores em uma imagem e todos os descritores na outra imagem;
3- Selecionar as melhores correspondências para cada descritor de uma imagem;
4- Executar o RANSAC para estimar a homografia;
5- Juntar as imagens.

'''

# 1) Feature Detection com ORB
image1 = cv.imread('images/painel1.png')
image2 = cv.imread('images/painel2.png')

image1_grey = cv.cvtColor(image1, cv.COLOR_RGB2GRAY)
image2_grey = cv.cvtColor(image2, cv.COLOR_RGB2GRAY)

detect = cv.ORB_create()

keyPoint1, feat1 = detect.detectAndCompute(image1_grey, None)
keyPoint2, feat2 = detect.detectAndCompute(image2_grey, None)

# Desenhar os key points para demonstração. Esses pontos serão usados como referência para poder ser aplicado o image stitching
cv.imshow('Key Points 1', cv.drawKeypoints(image1, keyPoint1, None, color=(0,255,0)))
cv.imshow('Key Points 2', cv.drawKeypoints(image2, keyPoint2, None, color=(0,255,0)))

# 2) Achar as correspondecias entre as imagens com o BFMatcher.
'''
O brute-Force matcher pega o descritor de um recurso/feature da primeira imagem e combina com todos os outros recursos/features da segunda imagem usando algum cálculo de distância. E o mais próximo é retornado.
'''
bruteForce = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
best_matches = bruteForce.match(feat1, feat2)

raw_matches = sorted(best_matches, key=lambda x: x.distance)
print('Matches: ', len(raw_matches))

# Desenhar os pontos correspondentes
image3 = cv.drawMatches(image1, keyPoint1, image2, keyPoint2, best_matches[:100], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv.imshow('Pontos Correspondentes', image3)

# 3) Encontrar a perspectiva entre dois planos.
src_pts = np.float32([keyPoint1[m.queryIdx].pt for m in raw_matches]).reshape(-1,1,2)
dst_pts = np.float32([keyPoint2[m.trainIdx].pt for m in raw_matches]).reshape(-1,1,2)

H, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)

h,w = image1_grey.shape
pts = np.float32([[0,0], [0,h-1], [w-1, h-1], [w-1, 0]]).reshape(-1,1,2)
dst = cv.perspectiveTransform(pts, H)

# 4) Unir as imagens
image_final = cv.polylines(image2, [np.int32(dst)], True, 255, 1, cv.LINE_AA)

cv.imshow('Imagem Final', image_final)

cv.waitKey(0)
cv.destroyAllWindows()