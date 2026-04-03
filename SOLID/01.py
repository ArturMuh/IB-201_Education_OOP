import json
from dataclasses import dataclass


@dataclass
class Order:
    id: str
    price: float
    qty: int
    customer_email: str


class Load:
    def load_json_file(self, json_path: str) -> list:
        with open(json_path, "r", encoding="utf-8") as f:
            raw = json.load(f)
        return raw


class ValidateAndParse:
    def parse(self, raw: str) -> list[Order]:
        orders = []
        for item in raw:
            self._validate(item)
            orders.append(Order(item["id"], float(item["price"]), int(item["qty"]), item["email"]))
        return orders

    def _validate(self, item: dict) -> None:
        if "id" not in item or "price" not in item or "qty" not in item or "email" not in item:
            raise ValueError("Invalid order payload")
        if item["qty"] <= 0:
            raise ValueError("qty must be positive")


class Calc:
    def calculate_total(self, orders: list[Order]) -> float:
        total = sum(o.price * o.qty for o in orders)
        return total


class Format:
    def format_report(self, orders: list[Order], total: float) -> str:
        report = f"Orders count: {len(orders)}\nTotal: {total:.2f}\n"
        return report


class Send:
    def send_email(self, to: str, subject: str, body: str) -> None:
        print(f"[EMAIL to={to}] {subject}\n{body}")


class OrderReportService:
    def make_and_send_report(self, json_path: str) -> str:
        raw = Load().load_json_file(json_path)
        orders = ValidateAndParse().parse(raw)
        total = Calc().calculate_total(orders)
        report = Format().format_report(orders, total)
        for o in orders:
            Send().send_email(o.customer_email, "Your order report", report)
        return report