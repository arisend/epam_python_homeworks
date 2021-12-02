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
        def __init__(self):
            self.wrap = cls()
            next(self._ids)
        @classmethod
        def get_created_instances(self):
            return self._ids
        @classmethod
        def reset_instances_counter(self):
            _idsold=self._ids
            self._ids=count(0)
            return _idsold
    return Wrapper



@instances_counter
class User:
    pass