from collections.abc import Iterable


# class HofstadterSequence:
#     def __init__(self, s: list):
#         self.s = s[:]

def hofstadter_sequence(s):
    s = s[:]

    # try:
    q = s[-s[-1]] + s[-s[-2]]
    s.append(q)
    yield q
    # except IndexError:
    #     raise StopIteration()

    # def __iter__(self):
    #     return self
    #
    # def current_state(self):
    #     return self.s


seq = hofstadter_sequence([1, 1])

for _ in range(5):
    print(next(seq))



