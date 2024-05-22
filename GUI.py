from tkinter import *
from tkinter.filedialog import askopenfile
from main import recognize_image
from PIL import Image
import time

root = Tk()
root['bg'] = "#8b00ff"
root.title('Анализатор дорожных знаков')
root.wm_attributes('-alpha', 0.9)
root.geometry('900x500')
root.resizable(width=False, height=False)


text_output = Text(root, wrap=WORD, width=60, height=10)
text_output.place(x=200, y=50)

time_output = Text(root, wrap=WORD, width=60, height=3)
time_output.place(x=200, y=250)




def open_file():
    global img
    file = askopenfile(mode ='r', filetypes =[('Python Files', '*',)])
    if file is not None:
        img = file.name
        print(img)

btn_open_file = Button(root, text='Выбрать файл', command=open_file)
btn_open_file.place(x=420, y=400)

def start_program():

    start_time = time.time()
    
    result = recognize_image(img_path=img)
    end_time = time.time()
    total_time = end_time - start_time
    text_output.delete(1.0, END)  
    text_output.insert(END, f'Опознан: {result}') 

    time_output.delete(1.0, END)
    time_output.insert(END, f'Время выполнения: {total_time:.2f} сек')
    print("Запуск\n\n\n")


btn_start = Button(root, text='Запустить программу', command=start_program)
btn_start.place(x=420, y=350)

if __name__ == "__main__":
    root.mainloop()
