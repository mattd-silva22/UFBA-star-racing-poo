from typing import Optional
from tupy import *
import random

class Meteoro(BaseGroup):
    def __init__(self):
        super().__init__()
        self._add(Image('Meteors/meteoro1.png', y= random.randint(0,250)))
        self._add(Image('Meteors/meteoro2.png', y= random.randint(0,250)))
        self._add(Image('Meteors/meteoro3.png', y= random.randint(0,250)))
        self._add(Image('Meteors/meteoro4.png', y= random.randint(0,250)))
        self._add(Image('Meteors/meteoro1.png', y= random.randint(0,250)))
        self._add(Image('Meteors/meteoro2.png', y= random.randint(0,250)))
        self._add(Image('Meteors/meteoro3.png', y= random.randint(0,250)))
        self._add(Image('Meteors/meteoro4.png', y= random.randint(0,250)))
        self._add(Image('Meteors/meteoro1.png', y= random.randint(0,250)))
        self._add(Image('Meteors/meteoro2.png', y= random.randint(0,250)))
        self._add(Image('Meteors/meteoro3.png', y= random.randint(0,250)))
        self._add(Image('Meteors/meteoro5.png', y= random.randint(0,250)))
        self._hide()

    def move(self):
        self._y = (self._y + 15) % 540
        if self._y < 15:
            self._x = random.randrange(70, 800, 100)
            image = random.randint(1, 5)
            self._file = f'Meteors/meteoro{image}.png'
