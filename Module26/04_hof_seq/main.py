from collections.abc import Iterable


class HofstadterSequence:
    def __init__(self, s: list):
        self.s = s[:]

    def __next__(self) -> Iterable[int]:
        try:
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self

    # def current_state(self):
    #     return self.s


seq = HofstadterSequence([1, 1])

for _ in range(10):
    print(next(seq), end=' ')
