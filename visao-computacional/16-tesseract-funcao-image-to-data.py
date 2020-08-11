import cv2 as cv
import pytesseract

'''
image_to_data Retorna as palavras encontras na imagem delitimadas por boxes

Parametros:

image_to_data(image, lang=None, config='', nice=0, output_type=Output.STRING, timeout=0, pandas_config=None)

    image Object or String - Imagem. É preciso converter para RGB.
    lang String - Lingua do Tesseract deverá reconhecer. Defaults é eng. É possível multiplas linguas: lang='eng+fra'
    config String - Qualquer custom adicional configuração: config='--psm 6'
    nice Integer - modifica a prioridade do processador para a execução do Tesseract. Não suportado no Windows. Nice ajusta a gentileza de processos do tipo unix.
    output_type Atributo de classe - especifica o tipo de saída, o padrão é string. Para obter a lista completa de todos os tipos suportados, verifique a definição de classe pytesseract.Output.
    timeout Integer or Float - duração em segundos para o processamento do OCR, após o qual o pytesseract será encerrado e aumentará o RuntimeError.
    pandas_config Dict - somente para o tipo Output.DATAFRAME. Dicionário com argumentos personalizados para pandas.read_csv. Permite personalizar a saída de image_to_data.
'''

image = cv.imread('images/placa_cortada.png')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

boxes = pytesseract.image_to_data(image)

# Percorrer os boxes desenhar os retângulos e textos nas palavras completas, ao invés de letra por letra
for a,b in enumerate(boxes.splitlines()):
        print(b)
        if a!=0: # Se existir alguma palavra
            b = b.split()
            if len(b)==12: # a matriz contendo 12 colunas, significa que existe alguma palavra encontrada
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                cv.putText(image,b[11],(x,y-5),cv.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
                cv.rectangle(image, (x,y), (x+w, y+h), (50, 50, 255), 2)

cv.imshow('Imagem com retângulos', image)
cv.waitKey(0)
cv.destroyAllWindows()