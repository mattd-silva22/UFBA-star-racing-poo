from tupy import *
from time import sleep

class Button(Image):
    def __init__(self, x, y, file):
        self.file = file
        self.x = x
        self.y = y
        self.is_clicked = False

    def update(self):
        if (self.x <  mouse.x < self.x + 80) and (self.y < mouse.y < self.y + 80):
            if mouse.is_button_down():
                sleep(0.01)
                self.click()

    def click(self):
        self.is_clicked = not self.is_clicked

if __name__ == '__main__':
    pause_button = Button("Pausar", 10, 10, "pausa.png")
    restart_button = Button("Reiniciar", 10, 10, "return.png")

    print(dir(pause_button))
    pause_button.click()