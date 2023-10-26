import releword as rw
import model

inputFileName = input("Введите имя файла с текстом для обработки: ")
modelFileName = input("Введите имя файла с моделью обучения: ")

intents, predicts = model.model(inputFileName, modelFileName)
for i in range(len(intents)):
    print(f"{rw.find_phrases(intents[i])} - {predicts[i].strip()}")



