from customtkinter import *
from pyautogui import typewrite
from pyautogui import press
from time import sleep

def spam():
    sleep(5)
    zero = float(0)
    timeee = float(time.get())
    numberrr = float(number.get())
    phraseee = phrase.get()
    while zero<numberrr:
        numberrr = numberrr - (1)
        typewrite(phraseee)
        press('enter')
        sleep(timeee)





set_default_color_theme('green')
set_appearance_mode('dark')
window = CTk()
window.geometry('400x400')
window.resizable(False,False)
window.title('Spammer')
phrasee = CTkLabel(window,text="The phrase to spam",height=15,font=("Rubik",15)).pack()
phrase = CTkEntry(window,placeholder_text="ex:hello",height=5)
phrase.pack(padx=10,pady=10)
timee = CTkLabel(window,text="Time between messages",height=15,font=("Rubik",15)).pack()
time = CTkEntry(window,placeholder_text="ex:0",height=5)
time.pack(padx=10,pady=10)
numberr = CTkLabel(window,text="How many times to send the phrase",height=15,font=("Rubik",15)).pack()
number = CTkEntry(window,placeholder_text="ex:50",height=5)
number.pack(padx=10,pady=10)


start = CTkButton(window,text="Start\n5 sec delay",command=spam).pack(padx=10,pady=10)

window.mainloop()