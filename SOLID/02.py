from dataclasses import dataclass
from abc import ABCMeta, abstractmethod


@dataclass
class Order:
    total: float


class Discount:
    @abstractmethod
    def get_discount_price(self, order: Order) -> float:
        pass


class RegularDiscount(Discount):
    def get_discount_price(self, order: Order) -> float:
        return order.total


class VIPDiscount(Discount):
    def get_discount_price(self, order: Order) -> float:
        return order.total * 0.9


class EmployeeDiscount(Discount):
    def get_discount_price(self, order: Order) -> float:
        return order.total * 0.8


class DiscountFactory:
    _discounts = {
        "regular": RegularDiscount,
        "vip": VIPDiscount,
        "employee": EmployeeDiscount
    }

    @classmethod
    def get_discount(cls, customer_kind: str) -> Discount:
        discount_class = cls._discounts.get(customer_kind, RegularDiscount)
        return discount_class()

    @classmethod
    def register_discount(cls, kind: str, discount_class):
        cls._discounts[kind] = discount_class


@dataclass
class Customer:
    kind: 'Discount'

def apply_discount(order: Order, customer: Customer) -> float:
    return customer.kind.get_discount_price(order)


class BlackFridayDiscount(Discount):
    def get_discount_price(self, order: Order) -> float:
        return order.total * 0.5