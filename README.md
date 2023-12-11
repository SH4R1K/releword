Продукт был создан в рамках Хакатона за 3 дня.  
Releword - продукт создан для семантического анализа текста и определение значения слова: прямое оно или переносное. 
	Для работы с модулем нужно установить сторонние библиотеки:  
 -Natasha
 -Pymorphy2
 -Re
 -skelern
 -scikit-learn
В модуле представлено машинное обучение с помощью метрики TF-IDF, и реализованы следующие функции:	
 - find_phrases(string: text) - функция для нахождения словосочетаний | возвращает строковое значение
 - get_list_sentences(string: fileName) -  получение списка предложений | возвращает список предложений

Подключение производится через import
___________________________________________________________________________________
import releword
import model

___________________________________________________________________________________
 
Model - это библиотека которая использовалась для создания модели обучения

Пример кода создания модели обучения
inputFileName = “Filename.txt”
modelFileName = “modelFilename.txt”

intents, predicts = model.model(inputFileName, modelFileName)
___________________________________________________________________________________
