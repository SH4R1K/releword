import releword as rw
import model

inputFileName = input("Введите имя файла с текстом для обработки: ")
modelFileName = input("Введите имя файла с моделью обучения: ")

types = ["прямое значение", "переносное значение сущ.", "переносное значение прил."]
intents, predicts = model.model(inputFileName, modelFileName)
for type in types:
    for i in range(len(intents)):
        if (predicts[i].strip() == type):
            print(f"{i}.{rw.find_phrases(intents[i])} - {predicts[i].strip()}")



