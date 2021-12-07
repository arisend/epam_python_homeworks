"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""
from itertools import count


def instances_counter(cls):
    class Wrapper:
        _ids = count(0)
        strId = 0

        def __init__(self):
            self.wrap = cls()
            Wrapper.strId = next(self._ids) + 1

        @classmethod
        def get_created_instances(self):
            return self.strId

        @classmethod
        def reset_instances_counter(self):
            _idsold = self.strId
            self._ids = count(0)
            self.strId = 0
            return _idsold

    return Wrapper


@instances_counter
class User:
    pass


if __name__ == '__main__':
    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
    user.get_created_instances()
