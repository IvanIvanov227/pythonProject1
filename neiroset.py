from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Создаём объект последовательное модели нейронной сети
model = Sequential()

# Помещаем необходимые слои в модель
# Слой, обрабатывающий входные данные, размерностью 784 элемента.
# Количество нейронов в слое зададим 700, а функцию активации 'relu'
model.add(Dense(units=700,
                input_dim=784,
                activation='relu'))

# Выходной слой, выдающий вероятность принадлежности к одному из 5 классов с функцией активации 'softmax'
model.add(Dense(5, activation='softmax'))