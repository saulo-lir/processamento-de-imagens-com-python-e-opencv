import numpy as np
import cv2

# 1) Definir o intervalo de cor que pretendemos rastrear

            # Criação de um array
azulEscuro = np.array([100,67,0], dtype="uint8")
azulClaro = np.array([255,128,50], dtype="uint8")

# Capturar o objeto, que no caso estará contido num vídeo
            # O parâmetro 0 corresponde a webcam
camera = cv2.VideoCapture(0)

# Os frames do vídeo devem ser capturados em loop infinito
while True:
    (sucesso, frame) = camera.read()

    if not sucesso:
        break

    # Aplicar limiarização. Na janela capturada, tudo que estiver no intervalo de cor azulEscuro e azulClaro, será exibido em escala cinza, e tudo que não for, não será exibido, ou seja, a tela ficará na cor preta.
    obj = cv2.inRange(frame, azulEscuro, azulClaro)

    # Identificar os contornos do objeto
    (contornos, _) = cv2.findContours(obj.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contornos) > 0:
        cnt = sorted(contornos, key=cv2.contourArea, reverse=True)[0]

        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
        cv2.drawContours(frame, [rect], -1, (0,255,255), 2)

    # Exibir a filmagem da webcam
    cv2.imshow("Janela 1", frame)
    cv2.imshow("Janela 2", obj)

    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

camera.release()
cv2.destroyAllWindows()