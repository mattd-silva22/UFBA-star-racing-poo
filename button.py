from tupy import *
from time import sleep

class Button(Image):
    def __init__(self, x: int, y: int, file: str) -> None:
        self.file = file
        self.x = x
        self.y = y
        self.is_clicked = False

    def update(self) -> None:
        if (self.x <  mouse.x < self.x + 80) and (self.y < mouse.y < self.y + 80):
            if mouse.is_button_down():
                sleep(0.01)
                self.click()

    def click(self) -> None:
        self.is_clicked = not self.is_clicked
    
    def get_state(self) -> bool:
        return self.is_clicked
    
    def reset_state(self) -> None:
        self.is_clicked = False
        
if __name__ == '__main__':
    pause_button = Button(10, 10, "pausa.png")
    restart_button = Button(10, 10, "return.png")

    print(dir(pause_button))
    pause_button.click()