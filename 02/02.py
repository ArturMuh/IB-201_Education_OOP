class LeftParagraph:
    def __init__(self, width: int):
        self.width = width # ширина строки
        self.word = [] # это хранение массива

    def add_word(self, word: str) -> None:
        if not self.word:
            self.word.append(word)
        elif len(self.word[-1] + ' ' + word) <= self.width: # добавление слова
            self.word[-1] += ' ' + word
        else:
            self.word.append(word)

    def end(self):
        print('\n'.join(self.word))


class RightParagraph:
    def __init__(self, width: int):
        self.width = width
        self.word = ['']

    def add_word(self, word: str) -> None:
        if len(self.word[-1] + ' ' + word) <= self.width:
            self.word[-1] += ' ' + word if self.word[-1] else word
        else:
            self.word.append(word)

    def end(self):
        print('\n'.join([line.rjust(self.width) for line in self.word]))


lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()