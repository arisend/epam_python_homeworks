"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 75
order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self, price, strategy):
        self.price = price
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The context stores a link to one of the Strategy objects. The context doesn't know
        specific class of strategy. It must work with all strategies
        through the Strategy interface.
        """

        return self._strategy

    def final_price(self):
        return self._strategy.calculate_final_price(self.price)


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    some algorithm.

    The context uses this interface to invoke the algorithm defined by
    Specific Strategies.
    """

    @abstractmethod
    def calculate_final_price(self, data: float):
        pass


class Morning_discount(Strategy):
    def calculate_final_price(self, price: float) -> float:
        discount = 0.25
        return price - price * discount


class Elder_discount(Strategy):
    def calculate_final_price(self, price: float) -> float:
        discount = 0.9
        return price - price * discount
