from dataclasses import dataclass, field, make_dataclass

class Car:

    def __init__(self, model, max_speed, price):
        self.model = model
        self.max_speed = max_speed
        self.price = price

    def get_max_speed(self):
        return self.max_speed

@dataclass
class CarD:
    model:str
    max_speed: int | float
    price: int = field(default=0)

    def get_max_speed(self):
        return self.max_speed

    def get_price(self):
        return self.price

CarData = make_dataclass("CarData", [('Model', str), "max_speed", ("price", int, field(default=0))],
                         namespace={"get_max_speed": lambda self: self.max_speed,
                                    'get_price': lambda self: self.price})

cd = CarData('Lada Granta', 120, 6000000)
print(cd.get_max_speed())
print(cd.get_price())