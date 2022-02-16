from typing import List


def main() -> None:
    strings: List[str] = ['a', 'b', 'c', 'd', 'e']
    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

    results = [(strings[i], numbers[i]) for i in range(min(len(strings), len(numbers)))]
    print(results)

    # лучше так
    results2 = list(map(lambda x, y: (x, y), strings, numbers))
    print(results2)


if __name__ == '__main__':
    main()
