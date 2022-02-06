from typing import Optional, Any


class Node:
    def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return 'Node [{value}]'.format(
            value=str(self.value)
        )


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def __str__(self) -> str:
        if self.head is not None:
            current = self.head
            values = [str(current.value)]

            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return '[{values}]'.format(values=' '.join(values))
        return 'LikedList []'

    def append(self, elem: Any) -> None:
        new_node = Node(elem)

        if self.head is None:
            self.head = new_node
            return

        last = self.head

        while last.next:
            last = last.next

        last.next = new_node
        self.length += 1

    def remove(self, index) -> None:
        cur_node = self.head
        cur_index = 0

        # Если список пустой, или индекс вне диапазона выбрасываем ошибку.
        if self.length == 0 or self.length < index:
            raise IndexError()

        # Если узел не пустой и удаляем первый элемент:
        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.length -= 1
                return

        while cur_node is not None:
            # Индекс найден, идем дальше
            if cur_index == index:
                break

            # Перебираем все элементы, до нужного индекса
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1

        # Указатель на следующий элемент
        prev.next = cur_node.next
        self.length -= 1


my_list = LinkedList()

my_list.append(10)
my_list.append(20)
my_list.append(30)

print(my_list)

my_list.remove(1)

print(my_list)
