'''
Concept: 
High-level modules should not depend on low-level modules. Both should depend on 
abstractions. Also, abstractions should not depend on details; 
details should depend on abstractions.

Real-World Analogy: Like using a standard power socket in your home 
- The socket (high-level module) doesn't need to know type of device.
- The device (low-level module) is designed to fit the socket.

In Practice: 
A class should receive its dependencies from the outside rather 
than creating them itself. This can be achieved using interfaces or abstract 
classes, making the code more flexible and easier to test.

Example: To follow the Dependency Inversion Principle, we should depend on 
abstractions rather than concrete classes:
'''

from abc import ABC, abstractmethod

# Abstraction: EmailService
class EmailService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class SMTPService(EmailService):
    def send(self, message):
        print(f"Sending email via SMTP: {message}")

class MockEmailService(EmailService):
    def send(self, message):
        print(f"Mock sending email: {message}")

class EmailSender:
    # Dependency Inversion: EmailSender depends on EmailService (Abstraction)
    def __init__(self, email_service: EmailService):
        self.email_service = email_service
    
    def send_email(self, message):
        self.email_service.send(message)

# Example usage
smtp_service = SMTPService()
email_sender = EmailSender(smtp_service)
email_sender.send_email("Hello World")