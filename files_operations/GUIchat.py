from tkinter import *
from tkinter import scrolledtext


def get_data():
    with open('chat.txt', 'r', encoding = 'utf-8') as in_file:
        data = in_file.read()
    return data


window = Tk()
window.title("GUI chat.")

window.geometry('350x500')
txt = scrolledtext.ScrolledText(window, width = 40, height = 27)
txt.grid(column = 0, row = 0)
txt.insert(INSERT, get_data())
window.mainloop()
