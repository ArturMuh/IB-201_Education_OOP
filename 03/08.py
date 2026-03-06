class Queue:
    def __init__(self, *queue: int) -> None:
        self.queue = list(queue)

    def append(self, *values: int) -> None:
        self.queue.extend(values)

    def copy(self) -> 'Queue':
        return Queue(*self.queue)

    def pop(self) -> None:
        return self.queue.pop(0) if self.queue else None

    def extend(self, other: 'Queue') -> None:
        self.queue.extend(other.queue)

    def next(self) -> 'Queue':
        return Queue(*self.queue[1:]) if self.queue else Queue()

    def __add__(self, other: 'Queue') -> 'Queue':
        return Queue(*(self.queue + other.queue))

    def __iadd__(self, other: 'Queue') -> 'Queue':
        self.queue.extend(other.queue)
        return self

    def __eq__(self, other: 'Queue') -> bool:
        return self.queue == other.queue

    def __rshift__(self, n: int) -> 'Queue':
        return Queue(*self.queue[n:]) if n < len(self.queue) else Queue()

    def __str__(self) -> str:
        if not self.queue:
            return '[]'
        return '[' + ' -> '.join(map(str, self.queue)) + ']'

    def __next__(self) -> 'Queue':
        return self.next()

q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep = '\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)