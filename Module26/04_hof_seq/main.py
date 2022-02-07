from typing import Iterable


def hofstadter_sequence(s: list, count_print: int) -> Iterable[int]:
    s = s[:]

    try:

        if s == [1, 2]:
            return

        for index in range(count_print):
            q = s[-s[-1]] + s[-s[-2]]
            s.append(q)
            yield q

    except IndexError:
        return


def main():
    seq = hofstadter_sequence(s=[1, 1], count_print=20)

    for x in seq:
        print(x, end=' ')


main()
