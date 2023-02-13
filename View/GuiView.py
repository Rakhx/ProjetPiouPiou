from ProjectPiouPiou.View.AbstractView import AbstractView
from tkinter import Tk, Canvas, PhotoImage, mainloop
import time

class GuiView(AbstractView):
    # construction d'une fenetre de base
    def __init__(self):
        self.root = Tk()
        self._canvas = Canvas(self.root, width=1000, height=500, bg="#000000")
        self._canvas.pack()
        self.img = PhotoImage(width=1000, height=500)
        self._canvas.create_image((1000 , 500), image=self.img, state="normal")

        self.cpt = 0
        self._offset = 10

    def displayLand(self, representation):

        self._canvas.create_image((500 , 500), image=self.img, state="normal")
        lignes = representation.split('\n')
        actualY = 0
        for ligne in lignes:
            actualX = 0
            #caractere par caractere
            for c in ligne:

                self.draw(c, actualX, actualY)
                #print(c)
                # on se décale d'un offset sur la meme ligne
                actualX += self._offset

            # on passe une ligne sur les Y
            actualY += self._offset

        self.root.update()

    def draw(self, char, x, y):
        for xMoving in range(x, x + self._offset):
            for yMoving in range(y, y + self._offset):
                if char ==  '-':
                    #[print(xMoving, yMoving) for yMoving in range(y, y+self._offset)  for xMoving in range(x, x+self._offset)]
                   # [self.img.put("#777777", (xMoving,yMoving)) for yMoving in range(y, y+self._offset)  for xMoving in range(x, x+self._offset)]
                   self.img.put("#777777", (xMoving, yMoving))

                if char == 'o':
                    self.img.put("#333333", (xMoving, yMoving))

                if char == '>':
                    self.img.put("#000000", (xMoving, yMoving))
                if char == 'x':
                    self.img.put("#FF00FF", (xMoving, yMoving))




