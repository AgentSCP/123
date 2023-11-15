from dataclasses import dataclass

@dataclass
class AirCastle:
    height: int
    blocks: int
    color: str

    def chance_height(self, value):
        self.height = value if value >= 1 else 0

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError("Error")
        self.blocks = self.blocks + other
        self.height = self.height + other // 5

        return AirCastle(self.height, self.blocks, self.color)

    def visible(self, visibli):
        return f'Видимость замка: {self.height//visibli+self.blocks}'

    def __str__(self):
        return f"The AirCastle at an altitube of {self.height} meters, is {self.color} with {self.blocks} clouds"

v = AirCastle(200, 1200, "Red")
print(v)
v = v + 10
print(v)
