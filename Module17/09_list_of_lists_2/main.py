def main():
    nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                 [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

    result_list = [item for outer_group in nice_list for inner_group in outer_group for item in inner_group]
    print(result_list)


if __name__ == '__main__':
    main()
