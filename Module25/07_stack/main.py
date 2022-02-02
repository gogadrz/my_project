class OtherStack:
    def __init__(self):
        self.__storage = list()

    def push(self, value):
        self.__storage.append(value)

    def pop(self):
        if len(self.__storage) == 0:
            return False
        else:
            return self.__storage.pop()


class TaskManager:

    def __init__(self):
        self.__data_storage = OtherStack()
        self.__item_count = 0

    def new_task(self, task, priority):
        self.__data_storage.push((priority, task))
        self.__item_count += 1

    def remove_task(self, rem_task, rem_priority):
        self.__item_count -= 1
        tmp_storage = OtherStack()

        for index in range(self.size()):
            line = self.__data_storage.pop()

            priority = line[0]
            task = line[1]

            if priority != rem_priority or task != rem_task:
                tmp_storage.push(line)

        while True:
            line = tmp_storage.pop()
            if not line:
                break
            self.__data_storage.push(line)

    def size(self):
        return self.__item_count

    def __str__(self):
        tmp_storage = OtherStack()
        result_dict = dict()
        result_str = ''

        for index in range(self.size()):

            line = self.__data_storage.pop()
            tmp_storage.push(line)

            priority = line[0]
            task = line[1]

            if priority in result_dict:
                save_task = result_dict[priority]
                result_dict[priority] = '{task}; {save_task}'.format(
                    task=task,
                    save_task=save_task
                )
            else:
                result_dict[priority] = task

        for key, value in sorted(result_dict.items()):
            result_str += '{key} {value}\n'.format(
                key=key,
                value=value
            )

        while True:
            line = tmp_storage.pop()
            if not line:
                break
            self.__data_storage.push(line)

        return result_str


def main():
    manager = TaskManager()

    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать дз", 2)

    print(manager)

    manager.remove_task("отдохнуть", 1)
    manager.remove_task("помыть посуду", 4)

    print(manager)


main()
