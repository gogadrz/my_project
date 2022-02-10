class File:
    def __init__(self, file_name: str, mode: str) -> None:
        self.__file_name = file_name
        self.__mode = mode
        self.__out_file = None

    def __enter__(self):
        self.__out_file = open(self.__file_name, self.__mode, encoding = 'utf-8')
        # print(type(self.__out_file))
        return self.__out_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__out_file.close()


def main():
    with File('../example.txt', 'w') as file:
        file.write('Всем привет!')

    if file.closed:
        print('file is closed')


main()
