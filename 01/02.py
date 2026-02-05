class Button:
    def __init__(self):
        self.count = 0 # атрибут класса

    def click(self):
        self.count += 1 # увеличивает

    def click_count(self):
        return self.count

    def reset(self):
        self.count = 0 # здесь он обнуляет число


# button = Button()
# button.click()
# button.click()
# print(button.click_count())
# button.click()
# print(button.click_count())

# button = Button()
# button.click()
# button.click()
# print(button.click_count())
# button.reset()
# button.click()
# print(button.click_count())

button = Button()
button.click()
print(button.click_count())