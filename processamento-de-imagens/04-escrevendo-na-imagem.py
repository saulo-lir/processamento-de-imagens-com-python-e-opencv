import cv2

image = cv2.imread('images/piscina-bolinhas.jpg')

# Definindo o tipo da fonte
fonte = cv2.FONT_HERSHEY_COMPLEX

# Escrever texto na imagem:
                        # Início do texo (y,x)
cv2.putText(image, 'Gandalf', (50, 50), fonte, 2, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('Imagem', image)
cv2.waitKey(0)