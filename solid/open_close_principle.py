'''
Concept: 
Software entities (classes, modules, functions, etc.) should be open for 
extension, but closed for modification.

Real world situation: 
We have a software to handle payment requests, we can add new payment methods 
without changing the existing payment handling code.

In Practice: Implementing new functionalities via interfaces or abstract classes
, allowing new functionalities to be added without changing existing code.

Eample:
To follow the Open/Closed Principle, we can use abstract classes and inheritance 
to add new payment types without changing existing code:
'''

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f'Processing credit card payment: {amount}')

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f'Processing PayPal payment: {amount}')

class PaymentProcessor:
    def process_payment(self, payment: Payment, amount):
        payment.process_payment(amount)

# Example usage
credits_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

payment_processor = PaymentProcessor()

# Output: Processing credit card payment: 100
payment_processor.process_payment(credits_card_payment, 100)  
# Output: Processing PayPal payment: 200
payment_processor.process_payment(paypal_payment, 200)    