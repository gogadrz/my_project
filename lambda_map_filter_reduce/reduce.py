from functools import reduce
from typing import List

#
# def my_add(a: int, b: int) -> int:
#     result = a + b
#     print(f"{a} + {b} = {result}")
#     return result
#
#
# numbers: List[int] = [0, 1, 2, 3, 4]
# print(reduce(my_add, numbers))
# ==============================================
#
# Используя функцию reduce, реализуйте код, который считает,
# сколько раз слово was встречается в списке:

sentences = ["Nory was a Catholic",
             "because her mother was a Catholic",
             "and Nory’s mother was a Catholic",
             "because her father was a Catholic",
             "and her father was a Catholic",
             "because his mother was a Catholic",
             "or had been"]


print(reduce(lambda a, b: a + b, [i.lower().split().count('was') for i in sentences]))
