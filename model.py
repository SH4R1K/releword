from sklearn.feature_extraction.text import TfidfVectorizer  # skleran для классификации текста
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
import numpy as np  # numpy для работы с массивами
import releword as rw


def load(modelFileName):
    data = {'intent': [], 'response': []}  # словарь для хранения данных

    with open(modelFileName, "r", encoding="utf-8") as file:  # открываем файл с данными
        for line in file:  # читаем файл построчно
            row = line.split("|")  # разбиваем строку на массив
            data['intent'] += [row[0]]  # добавляем вопрос в словарь
            data['response'] += [row[1]]  # добавляем ответ в словарь

    return data

def train_test_split(data, validation_split=0.2):  # функция разбиения выборки на обучающую и тестовую. validation_split - доля тестовой выборки
    size = len(data['intent'])  # размер выборки
    indices = np.arange(size)  # создаем массив индексов
    np.random.shuffle(indices)  # перемешиваем массив индексов

    x = [data['intent'][i] for i in indices]  # создание массива из текстов
    y = [data['response'][i] for i in indices]  # создание массива из ответов
    validation_samples = int(validation_split * size)  # определяем размер валидационной выборки

    return {
        'train': {'x': x[:-validation_samples], 'y': y[:-validation_samples]},  # обучающая выборка
        'test': {'x': x[-validation_samples:], 'y': y[-validation_samples:]}  # тестовая выборка
    }


def model(inputFileName, modelFileName):
    data = load(modelFileName)  # загружаем данные
    sample = train_test_split(data)  # разбиваем выборку на обучающую и тестовую
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),  # tfidf векторизация текста (преобразование текста в вектор)
        ('clf', SGDClassifier(loss='hinge'))  # классификатор (метод опорных векторов) с функцией потерь hinge нужен для классификации текста
    ])  # создаем модель

    pipeline.fit(sample['train']['x'], sample['train']['y'])  # обучаем модель
    intents = rw.get_list_sentences(inputFileName)
    predicted = pipeline.predict(intents)
    return intents, predicted