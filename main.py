import tkinter as tk
from tkinter import ttk
import sys

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes("-alpha" ,1) #прозрачность
        self.attributes("-topmost", True) #поверх всех окон
        self.overrideredirect(True) #убрать рамку
        self.resizable(False, False) #запрет растягивания
        self.title("CPU-RAM usage monitor")
        self.set_ui()

    def set_ui(self):
        #кнопка выхода
        self.exit_button = ttk.Button(self, text="Exit", command=self.appExit)
        self.exit_button.pack(fill=tk.X) # заполнение по X

        #создаем рамку
        self.manual_frame = ttk.LabelFrame(self, text="Manual")
        self.manual_frame.pack(fill=tk.X)

        #список состояний окна
        self.combo_window_states = ttk.Combobox(self.manual_frame,
                                                values=["hide", "don't hide", "min"],
                                                width=9,
                                                state="readonly")
        self.combo_window_states.current(1)
        self.combo_window_states.pack(side=tk.LEFT)

        #кнопка в рамке
        self.manual_button = ttk.Button(self.manual_frame, text='Move').pack(side=tk.LEFT)
        self.right_button = ttk.Button(self.manual_frame, text='>>>').pack(side=tk.LEFT)

        # создаем рамку
        self.power_frame = ttk.LabelFrame(self, text="Power")
        self.power_frame.pack(fill=tk.BOTH)
        #привязка событий мыши к главному окну
        self.bind_class("Tk", "<Enter>", self.mouseEnter)
        self.bind_class("Tk", "<Leave>", self.mouseLeave)

    #обработчики событий
    #выход
    def appExit(self):
        self.destroy()
        sys.exit()
    #мышь над главным окном
    def mouseEnter(self, event):
        if self.combo_window_states.current() == 0 or 1:
            self.geometry("")
    #мышь уходит с главного окна
    def mouseLeave(self, event):
        if self.combo_window_states.current() == 0:
            self.geometry(f"{self.winfo_width()}x10")

def main():
    root = Application()
    root.mainloop()


if __name__ == '__main__':
    main()


