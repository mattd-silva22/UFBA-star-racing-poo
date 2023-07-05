from tupy import *
from time import sleep

class Star(Image):
    def __init__(self, star:int ) -> None:
        self.file = "Stars/star.png"
        self.x = (star + 1) * 40
        self.y = 450
