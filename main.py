from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# Загрузка моделей
model1 = load_model('model_2.h5') # модель на знаки

# Функция для распознавания изображения с использованием всех моделей
def recognize_image(img_path):
    # Загрузка изображения и преобразование его к необходимому размеру и формату
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # Масштабирование значений пикселей к диапазону [0, 1]



    prediction1 = model1.predict(img)

    

    array_answer = {prediction1[0][0]: 'Знак',
                    prediction1[0][1]: "Главная дорога",
                    prediction1[0][2]: "Пешеходный переход",
                    prediction1[0][3]: "Уступи дорогу" ,
                    prediction1[0][4]: "Нет знака"}

    max_choice = max(array_answer)

    print(f'1- класс {prediction1[0][0]} - знак какой-то :')
    print(f'2- класс {prediction1[0][1]} - знак Главная дорога:')
    print(f'3- класс {prediction1[0][2]} - знак Пешеходный переход:')
    print(f'4- класс {prediction1[0][3]} - знак Уступи дорогу:')
    print(f'5- класс {prediction1[0][4]} - Нет знака:')


    for answer in array_answer:
        if max_choice == answer:
            return array_answer[answer]