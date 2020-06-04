import cv2

#Link para download do arquivo Haarcascade https://github.com/opencv/opencv/tree/master/data/haarcascades

# 1) Definir função para redimensionar o vídeo para diminuir a carga de processamento
def redim(img, largura):
    alt = int(img.shape[0]/img.shape[1] * largura)
    img = cv2.resize(img, (largura, alt), interpolation=cv2.INTER_AREA)
    return img

# 2) Ler o arquivo de haarcascade. Esse arquivo contem a identificação de faces frontais.
df = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# 3) Ler um vídeo já gravado
camera = cv2.VideoCapture('video.mp4')

while True:
    (sucesso, frame) = camera.read()

    if not sucesso:
        break

    # Redimensionar os frames do video
    frame = redim(frame, 320)

    # Mudar a cor dos frames para preto e branco
    frame_pb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Identificar as faces humanas nos frames do vídeo
    faces = df.detectMultiScale(frame_pb, scaleFactor=1.1, minNeighbors=3, minSize=(20,20))
    frame_temp = frame.copy()

    # Desenhar um retângulo ao redor da face identificada
    for (x,y,lar,alt) in faces:
        cv2.rectangle(frame_temp, (x,y), (x+lar, y+alt), (0,255,255), 2)

    # Exibir o resultado na tela com o tamanho mais uma vez redimensionado, dessa vez para um tamanho maior
    cv2.imshow('Detector de Faces', redim(frame_temp, 640))

    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

camera.release()
cv2.destroyAllWindows()