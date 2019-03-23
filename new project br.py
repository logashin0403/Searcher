from tkinter import *
import time
import requests 
import json
import pyperclip
import webbrowser
import pyautogui as pt
from tkinter import messagebox



class won():
    
    def __init__(self):

        #время
        self.timeVar=StringVar()
        self.timeVar.set(time.strftime("%H%M%S.", time.localtime()))
        self.lbl1 = Label(tk, textvariable = self.timeVar , width = 16, anchor = "se", font = "arial 14 bold", bg = "#d9c0e3", fg = "#0c0755")
        self.lbl1.place(x = 174, y = 343)
        #время

        #дата
        self.dateVar = StringVar()
        self.dateVar.set(time.strftime("%d.%m.%Y", time.localtime()))
        self.lbl2 = Label(tk, textvariable = self.dateVar , width = 16, anchor = "se", font = "arial 14 bold", bg = "#d9c0e3", fg = "#0c0755")
        self.lbl2.place(x = 185, y = 368)
        #дата


        #поисковик
        self.ent = Entry(tk, width = 40, font = "arial 10 bold", bg = "#e2b7e0")
        self.ent.place(x = 60, y = 10)
        self.btn1 = Button(tk, text = "Найти", width = 5, bg = "#432042", fg = "#98ae7b", command = self.chit)
        self.btn1.place(x = 350, y = 8)
        
        #поисковик

        #курс долларов и евро
        self.money = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json() 
        self.text = json.dumps(str(self.money), sort_keys=True, indent=4) 
        self.parsed_string = json.loads(self.text) 
        self.mass = self.parsed_string.split() 
        self.USD = self.mass[184][:-3] 
        self.EUR = self.mass[199][:-1]
        self.usdVar = StringVar()
        self.usdVar.set(self.USD)
        self.lbl3 = Label(tk, textvariable = self.usdVar, width = 5, anchor = "sw", font = "arial 14 bold", bg = "#d9c0e3", fg = "#0c0755")
        self.lbl3.place(x = 153, y = 342)
        self.eurVar = StringVar()
        self.eurVar.set(self.EUR)
        self.lbl3 = Label(tk, textvariable = self.eurVar, width = 5, anchor = "sw", font = "arial 14 bold", bg = "#d9c0e3", fg = "#0c0755")
        self.lbl3.place(x = 153, y = 365)
        self.lbl4 = Label(tk, text = "Курс доллара:", width = 12, anchor = "sw", font = "arial 14 bold", bg = "#d9c0e3", fg = "#0c0755")
        self.lbl4.place(x = 5, y = 342)
        self.lbl5 = Label(tk, text = "Курс евро:", width = 9, anchor = "sw", font = "arial 14 bold", bg = "#d9c0e3", fg = "#0c0755")
        self.lbl5.place(x = 40, y = 365)        
        #курс долларов и евро

        
    #функция обновления даты и времени
        self.upd()
    def upd(self):
        self.timeVar.set(time.strftime("%H:%M:%S", time.localtime()))
        self.dateVar.set(time.strftime("%d.%m.%Y", time.localtime()))
        self.usdVar.set(self.USD)
        self.eurVar.set(self.EUR)
        self.lbl1.after(1000,self.upd)
    #функция обновления даты и времени

    def chit(self):
        messagebox.showinfo("Подсказка", "прочитайте и закройте сообщение  и через 5-6 секунд откроется браузер с вашим запросом)")
        self.a = self.ent.get()
        self.ent.delete(0, END)
        pyperclip.copy(self.a)
        webbrowser.open('http://yandex.com')
        time.sleep(8)
        pt.moveTo(542, 398, 0,1)
        pt.click(button='right')
        pt.moveTo(688, 512, 0,1)
        pt.click()
        pt.moveTo(967, 390, 0,1)
        pt.click()


            
tk = Tk()
tk.geometry("400x400+500+180")
tk.resizable(False,False)
tk.title("Панель помощи")
tk["bg"] = "#d9c0e3"
wn = won()
tk.mainloop()


