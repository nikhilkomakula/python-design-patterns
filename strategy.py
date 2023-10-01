"""
The Strategy Design Pattern is a behavioral design pattern that defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from the clients that use it.
"""

from typing import Type
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Credit Card")

class UPIPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using UPI")

class Order:
    def __init__(self, payment_strategy: Type[PaymentStrategy]) -> None:
        self._payment_strategy = payment_strategy

    def finalize_order(self, amount: float) -> None:
        self._payment_strategy.pay(amount)

# choose credit card payment strategy to make an order
order = Order(CreditCardPayment())

# make an order
order.finalize_order(100)

# choose UPI payment strategy to make an order
order = Order(UPIPayment())

# make an order
order.finalize_order(100)
