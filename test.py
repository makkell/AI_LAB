from main import recognize_image
import os


count = 0

array_correct_answer = []
array_not_correct_answer = []

directory = "Test2"

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        result = recognize_image(f)
        if result in filename:
            count += 1
            array_correct_answer.append(f'Ответ модели :{result} - Ожидалось {filename}')
        else:
            array_not_correct_answer.append(f'Ответ модели :{result} - Ожидалось {filename}')
        
print(f'Точность на тесте {count / 50 * 100}%')

print("Правильные ответы")
for arr in array_correct_answer:
    print(arr)

print()

print("Не правильные ответы")
for arr in array_not_correct_answer:
    print(arr)
        

