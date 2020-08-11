import cv2 as cv
import pytesseract

'''
image_to_boxes Retorna resultado contendo caracteres reconhecidos e seus boxes
'''

image = cv.imread('images/placa_cortada.png')

# O tesseract trabalha com imagens RGB, então devemos converter a imagem para esse padrão
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

boxes = pytesseract.image_to_boxes(image)
print(boxes)

height, width, _ = image.shape

# Percorrer os boxes que foram encontrados
for boxe in boxes.splitlines():
    boxe = boxe.split(' ')
    #print(boxe)

    # Desenhar retângulos nas letras identificadas na imagem
    x,y,w,h = int(boxe[1]), int(boxe[2]), int(boxe[3]), int(boxe[4])
    cv.rectangle(image, (x, height - y), (w, height - h), (50, 50, 255), 2)

    # Escrever abaixo de cada retângulo a letra correspondente
    cv.putText(image, boxe[0], (x, height - y+25), cv.FONT_HERSHEY_SIMPLEX, 1, (50,50,255), 2)

cv.imshow('Imagem com retângulos', image)
cv.waitKey(0)
cv.destroyAllWindows()