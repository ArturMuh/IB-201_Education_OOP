class ReversedList:
    def __init__(self, lst: list) -> None:
        self._list = lst

    def __len__(self) -> int:
        return len(self._list)

    def __getitem__(self, key):
        return self._list[len(self._list) - 1 - key]

rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])

rl = ReversedList([])
print(len(rl))

rl = ReversedList([10])
print(len(rl))
print(rl[0])
