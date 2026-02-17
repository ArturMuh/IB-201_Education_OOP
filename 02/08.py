class Person:
    def __init__(self, name: str, middle_name: str, last_name: str, phone_numbers: dict):
        self.name = name
        self.middle_name = middle_name
        self.last_name = last_name
        self.phone_numbers = phone_numbers

    def get_phone(self) -> int | None:
        return self.phone_numbers.get('private')

    def get_name(self) -> str:
        return ' '.join([self.last_name, self.name, self.middle_name])

    def get_work_phone(self) -> int | None:
        return self.phone_numbers.get('work')

    def get_sms_text(self) -> str:
        return f'Уважаемый {self.name} {self.middle_name}! Примите участие в нашем беспроигрышном конкурсе для физических лиц'


class Company:
    def __init__(self, name: str, type: str, phone_numbers: dict, *employees: Person):
        self.company_name = name
        self.company_type = type
        self.phone_numbers = phone_numbers
        self.employees = employees

    def get_phone(self) -> int | None:
        contact_number = self.phone_numbers.get('contact')
        if not contact_number:
            for person in self.employees:
                phone_number = person.phone_numbers.get('work')
                if phone_number:
                    return phone_number
            return None
        return contact_number

    def get_name(self) -> str:
        return self.company_name

    def get_sms_text(self) -> str:
        return f'Для компании {self.company_name} есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для {self.company_type}'


def send_sms(*objs: Person | Company) -> None:
    for obj in objs:
        number = obj.get_phone()
        obj_name = obj.get_name()
        sms_text = obj.get_sms_text()
        print(
            f'Отправлено СМС на номер {number} с текстом: {sms_text}' if number else f'Не удалось отправить сообщение абоненту: {obj_name}')
person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
person4 = Person("John", "Unknown", "Doe", {})
company1 = Company("Bell", "ООО", {"contact": 111}, person3, person4)
company2 = Company("Cell", "АО", {"non_contact": 222}, person2, person3)
company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)

person1 = Person("Степан", "Петрович", "Джобсов", {"private": 555})
person2 = Person("Боря", "Иванович", "Гейтсов", {"private": 777, "work": 888})
person3 = Person("Семен", "Робертович", "Возняцкий", {"work": 789})
person4 = Person("Леонид", "Арсенович", "Торвальдсон", {})
company1 = Company("Яблочный комбинат", "ООО", {"contact": 111}, person1, person3)
company2 = Company("ПластОкно", "АО", {"non_contact": 222}, person2)
company3 = Company("Пингвинья ферма", "Ltd", {"non_contact": 333}, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)


