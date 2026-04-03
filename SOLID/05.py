from abc import ABC, abstractmethod

class ANotification(ABC):
    @abstractmethod
    def send(self, to: str, text: str) -> None:
        pass

class EmailClient(ANotification):
    def send(self, to: str, text: str) -> None:
        print(f"[EMAIL to={to}] {text}")

class SmsClient(ANotification):
    def send(self, to: str, text: str) -> None:
        print(f"[SMS to={to}] {text}")

class PushNotifier(ANotification):
    def send(self, to: str, text: str) -> None:
        print(f"[PUSH to={to}] {text}")

class FakeNotifier(ANotification):
    def send(self, to: str, text: str) -> None:
        print(f"[FAKE] would send '{text}' to {to}")

class NotificationService:
    def __init__(self, email_notifier: ANotification, sms_notifier: ANotification):
        self.email_notifier = email_notifier
        self.sms_notifier = sms_notifier

    def notify(self, user_email: str, user_phone: str, text: str) -> None:
        self.email_notifier.send(user_email, text)
        self.sms_notifier.send(user_phone, text)

# Использование
service = NotificationService(
    email_notifier=EmailClient(),
    sms_notifier=SmsClient()
)
service.notify("IvanovPT@yandex.ru", "+792545259541", "Hello")
