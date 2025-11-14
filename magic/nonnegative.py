from typing import Any


class NonNegativeObject:
    def __init__(self, **kwargs: Any) -> None:
        for k in kwargs:
            value = abs(kwargs[k]) if isinstance(kwargs[k], (int, float)) else kwargs[k]
            setattr(self, k, value)

point = NonNegativeObject(x=1.5, y=-2.3, z=0.0,
color='yellow')
print(point.x)
print(point.y)
print(point.z)
print(point.color)