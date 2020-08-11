import cv2 as cv
import numpy as np
import imutils
import pytesseract

image = cv.imread('images/placa_1.jpg')

image = imutils.resize(image, width=500)
cv.imshow('Imagem Original', image)

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Imagem Em Cinza', grey)

# Aplicação do filtro bilateral
grey = cv.bilateralFilter(grey, 11, 17, 17)
cv.imshow('Imagem Filtrada Bilateral', grey)

# Detectar as bordas da imagem
edged = cv.Canny(grey, 170, 200)
cv.imshow('Imagem Filtrada', edged)

# Achar o contorno da imagem
_, contorno, _ = cv.findContours(edged.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#print(contorno)

# Desenhar o contorno
image2 = image.copy()
cv.drawContours(image2, contorno, -1, (0,255,0), 3)
cv.imshow('Imagem Contornos', image2)

# Identificar os 30 principais contornos
contorno = sorted(contorno, key = cv.contourArea, reverse = True)[:30]
numeroPlacaContorno = None

image3 = image.copy()
cv.drawContours(image3, contorno, -1, (0,255,0), 3)
cv.imshow('Imagem Top 30', image3)

# Identificar onde encontram-se os contornos da placa
count = 0
idx = 1

for c in contorno:
    perimetro = cv.arcLength(c, True)
    approx = cv.approxPolyDP(c, 0.02*perimetro, True)

    # Selecionar o contorno com 4 bordas, pois a placa é um retângulo
    if len(approx) == 4:
        numeroPlacaContorno = approx

        # Cortar os contornos encontrados, separando a placa da imagem
        x,y,w,h = cv.boundingRect(c)
        new_image = grey[y:y+h, x:x+w]
        cv.imshow('Placa Cortada', new_image)
        break

cropped_img_loc = 'images/placa_cortada.png'
#cv.imwrite(cropped_img_loc, new_image)

# Desenhar o contorno da placa na imagem original
cv.drawContours(image, [numeroPlacaContorno], -1, (0,255,0), 3)
cv.imshow('Imagem final com placa detectada', image)

cv.waitKey(0)
cv.destroyAllWindows()


# Aplicação do tesseract para reconhecimento dos caracteres da placa
'''
image_to_string Returns O resultado do Tesseract OCR em uma string que a imagem contém.
'''

text = pytesseract.image_to_string(cropped_img_loc, config = '-1 eng --oem 3 --psm 1')

print('Número da placa: ', text)