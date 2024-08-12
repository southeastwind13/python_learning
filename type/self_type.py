from typing import Self

class Shape:
    def __init__(self):
        self.scale =0.0

    def set_scale(self, scale: float) -> Self:
        self.scale = scale
        return self