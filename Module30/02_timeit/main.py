import timeit


def main() -> None:
    res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print(res)

    res_comprehensions: float = timeit.timeit("[''.join(str(i) for i in range(100))]", number=10000)
    print(res_comprehensions)

    res_map: float = timeit.timeit("[''.join(map(str, [a for a in range(100)]))]", number=10000)
    print(res_map)


if __name__ == '__main__':
    main()
