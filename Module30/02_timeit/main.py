import timeit


def main() -> None:
    res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print(res)

    res_comprehensions: float = timeit.timeit("[''.join(str(i) for i in range(100))]", number=10000)
    print(res_comprehensions)

    res_map: float = timeit.timeit("[''.join(map(str, [a for a in range(100)]))]", number=10000)
    print(res_map)

    # так короче, сразу указать range
    res9: float = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
    print(f'result with map {res:0.4}\n'.format(res=res9))


if __name__ == '__main__':
    main()
