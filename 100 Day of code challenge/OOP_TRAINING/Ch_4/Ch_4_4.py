from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    # def some_func(self, newval):
    #     self.value2 = newval


obj = ImmutableClass("Another String", 20)
print(obj.value1, obj.value2)

# obj.value1 = "Another String"
# print(obj.value1)

# obj.some_func(20)