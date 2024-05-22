import tensorflow as tf
from keras.applications import ResNet50
from keras.layers import Dense, GlobalAveragePooling2D, GlobalMaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D, MaxPooling2D
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam




# Загрузка предварительно обученной модели ResNet50 без верхних слоев
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

path_image = 'model_3/'  #  путь для подходящего формата строки

# Замена верхних слоев для классификации 
x = base_model.output
# x = GlobalAveragePooling2D()(x) # возможно стоит заменить на MaxPooling
# x = Dense(256, activation='relu')(x)

x = Conv2D(32, (3, 3), activation='relu', padding='same')(base_model.output)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = MaxPooling2D((2, 2))(x)

# Преобразование результатов в вектор
x = GlobalAveragePooling2D()(x)

predictions = Dense(5, activation='softmax')(x)  # Изменено на 2 нейрона и softmax
batch = 64
# Создание модели
model = tf.keras.Model(inputs=base_model.input, outputs=predictions)

# Заморозка базовой модели для обучения только верхних слоев
for layer in base_model.layers:
    layer.trainable = False


# Размораживаем верхние N слоев для обучения
N = 50
for layer in model.layers[-N:]:
    layer.trainable = True

for i, layer in enumerate(model.layers):
    print(i, layer.name)


# Компиляция модели

from keras.optimizers import Adam

# Уменьшаем скорость обучения до 0.0001

model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=['accuracy'])

# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])  

# Подготовка данных с использованием аугментации
data_generator = ImageDataGenerator(rescale=1./255, validation_split=0, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
train_generator = data_generator.flow_from_directory(
    path_image,
    target_size=(224, 224),
    batch_size=batch,
    subset='training',
    class_mode='categorical'  
)


test_generator = data_generator.flow_from_directory(
    path_image,
    target_size=(224, 224),
    batch_size=batch,
    subset='validation',
    shuffle=False,
    class_mode='categorical'  
)

# Обучение модели
history = model.fit(
    train_generator,

    epochs= 100
)

# # Оценка модели на тестовых данных
# test_loss, test_accuracy = model.evaluate(test_generator)
# print('Test Loss:', test_loss)
# print('Test Accuracy:', test_accuracy)

# Сохранение модели
# model.save('model_2.h5')


# Графики точности и потерь по эпохам
plt.plot(history.history['accuracy'], label='accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()

plt.plot(history.history['loss'], label='loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(loc='upper right')
plt.show()