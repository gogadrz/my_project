class Container:
    def __init__(self, value: any = None):
        self.value = value
        self.next_value = None

    def __str__(self) -> str:
        return '{}'.format(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: any) -> None:
        new_value = Container(value)

        if self.head is None:
            self.head = new_value
            return

        tail = self.head

        while tail.next_value:
            tail = tail.next_value

        tail.next_value = new_value

    def get(self, index: int) -> any:
        tail = self.head
        container_ndex = 0

        while container_ndex <= index:
            if container_ndex == index:
                return tail.value

            container_ndex = container_ndex + 1
            tail = tail.next_value

    def remove(self, rm_index: int) -> None:
        head = self.head
        last = head
        offset = 0

        if head is not None and rm_index == 0:
            self.head = head.next_value
            return

        while head is not None:
            if offset == rm_index:
                break
            offset += 1
            last = head
            head = head.next_value

        if head is None:
            return

        last.next_value = head.next_value

    def __str__(self) -> str:
        result = '['
        current_item = self.head

        while current_item is not None:
            result += f'{str(current_item.value)} '
            current_item = current_item.next_value

        return result[:-1] + ']'


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
