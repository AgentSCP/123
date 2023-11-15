from dataclasses import dataclass, field, InitVar

class Vector3D:

    def __init__(self, x, y, z, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x ** 2 + y ** 2 + z ** 2) ** 0.5 if calc_len else 0

@dataclass(order=True)
class VectorData:
    x: int
    y: int = field(compare=False)
    z: int = field(default=0)
    calc_len: InitVar[bool] = True
    length: float = field(init=False, default=0)
    pi: float = field(init=False)

    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        self.pi = 3.14


v = Vector3D(1,2,3)
print(v.__dict__)
vd = VectorData(1,4)
vd2 = VectorData(1,4)
print(vd == vd2)
print(vd)