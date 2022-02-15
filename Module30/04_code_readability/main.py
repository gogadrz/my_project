from typing import List


def simple_digits(top_limit: int) -> List[int]:

    simple: List[int] = list()
    cnt: int = 0

    for index in range(2, top_limit + 1):

        for divider in range(2, index + 1):

            if index % divider == 0:
                cnt += 1

        if cnt < 2:
            simple.append(index)

        cnt = 0
    return simple


def main():
    limit: int = 1000

    print(simple_digits(limit))
    print([x for x in range(2, limit) if not [t for t in range(2, x) if not x % t]])


if __name__ == '__main__':
    main()
