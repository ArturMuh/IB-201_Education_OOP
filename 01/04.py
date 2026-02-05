class OddEvenSeparator:
    def __init__(self):
        self.numbers = list()
        self.even_n = list()
        self.odd_n = list()

    def add_number(self, num):
        if num % 2 == 0:
            self.even_n.append(num)
        else:
            self.odd_n.append(num)


    def even(self):
        return self.even_n


    def odd(self):
        return self.odd_n

separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(5)
separator.add_number(6)
separator.add_number(8)
separator.add_number(3)
print(' '.join(map(str, separator.even())))
print(' '.join(map(str, separator.odd())))

