from tkinter import *
import tkinter as tk
import time

# Vue qui va être utilisée dans un thread à part pour l'affichage côté serveur
class ThreadedView():
    def __init__(self):
        self.root = Tk()
        self._canvas = Canvas(self.root, width=1000, height=500, bg="#000000")
        self._canvas.pack()
        # self.img = PhotoImage(width=1000, height=500)
        # self._canvas.create_image((1000, 500), image=self.img, state="normal")
        self.cpt = 0
        self._offset = 10

    def loop(self, data_lock, var):
        while True:
            time.sleep(2)
            self._canvas.delete()
            with data_lock:
                self.displayLand(var[0])

            self.root.update()

    def displayLand(self, representation):
        # self._canvas.create_image((500, 500), image=self.img, state="normal")
        lignes = representation.split('\n')
        actualY = 0
        for ligne in lignes:
            actualX = 0
            # caractere par caractere
            for c in ligne:
                self.draw(c, actualX, actualY)
                # on se décale d'un offset sur la meme ligne
                actualX += self._offset
            # on passe une ligne sur les Y
            actualY += self._offset

    def draw(self, char, x, y):
        if char == '-': # case vide - blanc
            self._canvas.create_rectangle(x, y, x + self._offset, y + self._offset, fill="#FFFFFF")
        if char == 'O': # Obstacle - noir
            self._canvas.create_rectangle(x, y, x + self._offset, y + self._offset, fill="#000000")
        if char == 'A': # Artilleur rose
            self._canvas.create_rectangle(x, y, x + self._offset, y + self._offset, fill="#800080")
        if char == 'M': # Marines fuccia
            self._canvas.create_rectangle(x, y, x + self._offset, y + self._offset, fill="#FF00FF")
        if char == 'E':
            self._canvas.create_rectangle(x, y, x + self._offset, y + self._offset, fill="#000000")
        if char == 'B':
            self._canvas.create_rectangle(x, y, x + self._offset, y + self._offset, fill="#FFFF00")
        if char == 'F': # Flag, rouge
            self._canvas.create_rectangle(x, y, x + self._offset, y + self._offset, fill="#FF0000")

