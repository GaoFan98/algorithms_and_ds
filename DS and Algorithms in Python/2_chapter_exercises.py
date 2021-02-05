# ################R-2.4################
# class Flower:
#     def __init__(self, name: str = None, num_of_petals: int = None, price: float = None):
#         self._name = name
#         self._petals = num_of_petals
#         self._price = price
#
#     def get_name(self):
#         if self._name is None:
#             return ("Name attribute is not found")
#         else:
#             return self._name
#
#     def get_petals(self):
#         if self._petals is None:
#             return ("Petals attribute is not found")
#         else:
#             return self._petals
#
#     def get_price(self):
#         if self._price is None:
#             return ("Price attribute is not found")
#         else:
#             return self._price
#
#     def set_name(self, name):
#         try:
#             self._name = name
#         except:
#             print("Name attribute must be string type")
#
#     def set_petals(self, petals):
#         try:
#             self._petals = int(petals)
#         except:
#             print("Petals attribute must be int type")
#
#     def set_price(self, price):
#         try:
#             self._price = int(price)
#         except:
#             print("Price attribute must be float type")
#
#
# Lily = Flower(22, num_of_petals="2", price="22")
# print(Lily.get_name(), Lily.get_petals(), Lily.get_price())
#
# Rose = Flower()
# Rose.set_name("FUCK THE PYTHON OOP, TOTAL BULLSHIT")
# Rose.set_petals("56.2")
# Rose.set_price("56.2")
# print(Rose.get_name(), Rose.get_petals(), Rose.get_price())

# ################P-2.34################
# class Doc():
#     def __init__(self, filepath):
#         self._path = filepath
#
#         self._read()
#
#     def _read(self):
#         with open(self._path, 'r') as file:
#             read = file.read().lower()
#             self._count_char(read)
#
#     def _count_char(self, value):
#         chars_dict = dict()
#
#         for char in value:
#             if ((ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90)):
#                 if char in chars_dict:
#                     chars_dict[char] += 1
#                 else:
#                     chars_dict[char] = 1
#
#         return self._plot(chars_dict)
#
#     def _plot(self, dict):
#         for key, value in sorted(dict.items()):
#             print(key, value * '=')
#
#
# Doc('test.txt')

# ################P-2.39################
# Copied from another repo, since it is not interesting task but someday would be useful
#
# from abc import abstractmethod, ABCMeta
# import math
#
#
# class Polygon(metaclass=ABCMeta):
#     def __init__(self, side_lengths=[1, 1, 1], num_sides=3):
#         self._side_lengths = side_lengths
#         self._num_sizes = 3
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#     def __repr__(self):
#         return (str(self._side_lengths))
#
#
# class Triangle(Polygon):
#     def __init__(self, side_lengths):
#         super().__init__(side_lengths, 3)
#         self._perimeter = self.perimeter()
#         self._area = self.area()
#
#     def perimeter(self):
#         return (sum(self._side_lengths))
#
#     def area(self):
#         s = self._perimeter / 2
#         product = s
#         for i in self._side_lengths:
#             product *= (s - i)
#         return product ** 0.5
#
#
# class EquilateralTriangle(Triangle):
#     def __init__(self, length):
#         super().__init__([length] * 3)
#
#
# t1 = Triangle([1, 2, 2])
# print(t1.perimeter(), t1.area())
#
# t2 = EquilateralTriangle(3)
# print(t2.perimeter(), t2.area())
# print(t2)
