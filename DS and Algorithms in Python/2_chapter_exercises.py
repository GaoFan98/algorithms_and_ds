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

# ################R-2.5################
