class SparseArray:
    def __init__(self):
        self.data = dict()

    def __setitem__(self, key: int, value: int) -> None:
        if value != 0:
            self.data[key] = value
        elif key in self.data:
            del self.data[key]

    def __getitem__(self, key: int) -> int:
        return self.data.get(key, 0)

arr = SparseArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print('arr[{}] = {}'.format(i, arr[i]))

arr = SparseArray()
arr[10] = 123
for i in range(8, 13):
    print('arr[{}] = {}'.format(i, arr[i]))

def print_elem(array, ind):
    print('arr[{}] = {}'.format(ind, array[ind]))


arr = SparseArray()
index = 1000000000
arr[index] = 123

print_elem(arr, index - 1)
print_elem(arr, index)
print_elem(arr, index + 1)