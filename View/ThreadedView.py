from tkinter import *
import tkinter as tk
import time

# Vue qui va être utilisée dans un thread à part pour l'affichage côté serveur
class ThreadedView():
    def __init__(self):
        self.ROOT = Tk()
        print("callOnce")
        LABEL = Label(self.ROOT, text="Hello, world!")
        LABEL.pack()

    def loop(self, data_lock ,var):
        while True:
            time.sleep(2)
            with data_lock:
                label = Label(self.ROOT, text=var[0])
            label.pack()
            self.ROOT.update()