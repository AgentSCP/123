from dataclasses import dataclass, field, InitVar
from typing import Any
from random import randint

@dataclass
class Goods:
    current_aid = 0

    uid: int = field(init=False)
    price: Any
    weight: Any

    def __post_init__(self):
        print("Goods")
        Goods.current_aid += 1
        self.uid = Goods.current_aid

class GoodMeassureFactory:

    @staticmethod
    def get_init_meassure():
        return [0,0,0]



@dataclass
class Book(Goods):
    title: str
    author: str
    price: int
    weight: float
    meassure: list = field(default_factory=GoodMeassureFactory.get_init_meassure)

    def __post_init__(self):
        super().__post_init__()
        print("Book")


g = Goods("512345632", 1200)
print(g)
b = Book(2000, 2.5, "qwerty", "xaxa")
for item in range(len(b.meassure)):
    b.meassure[1] = randint(10,20)

print(b)