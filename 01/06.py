class MinMaxWordFinder:

    def __init__(self):
        self.words = []
    def add_sentence(self, text):
        self.words += text.split()

    def shortest_words(self):
        min_dl = min(len(w) for w in self.words) if self.words else 0
        return sorted(w for w in self.words if len(w) == min_dl)

    def longest_words(self):
        max_dl = max(len(w) for w in self.words) if self.words else 0
        return sorted({w for w in self.words if len(w) == max_dl})


finder = MinMaxWordFinder()
finder.add_sentence('hello abc world')
finder.add_sentence('def asdf qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))

finder = MinMaxWordFinder()
finder.add_sentence('hello')
finder.add_sentence('abc')
finder.add_sentence('world')
finder.add_sentence('def')
finder.add_sentence('asdf')
finder.add_sentence('qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))

finder = MinMaxWordFinder()
finder.add_sentence('hello')
finder.add_sentence('  abc     def    ')
finder.add_sentence('world')
finder.add_sentence('            abc          ')
finder.add_sentence('asdf')
finder.add_sentence('qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))