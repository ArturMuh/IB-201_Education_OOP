import numpy as np
class Table:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.data = np.zeros((rows, cols), dtype=np.int16)

    def get_value(self, row: int, col: int) -> int | None:
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return int(self.data[row, col])
        return None

    def set_value(self, row: int, col: int, value: int) -> None:
        self.data[row, col] = value

    def n_rows(self) -> int:
        return self.rows

    def n_cols(self) -> int:
        return self.cols

    def delete_row(self, row: int) -> None:
        if 0 <= row < self.rows:
            self.data = np.delete(self.data, row, axis=0)
            self.rows -= 1

    def delete_col(self, col: int) -> None:
        if 0 <= col < self.cols:
            self.data = np.delete(self.data, col, axis=1)
            self.cols -= 1

    def add_row(self, row: int) -> None:
        if 0 <= row <= self.rows:
            new_row = np.zeros((1, self.cols), dtype=np.int16)
            self.data = np.insert(self.data, row, new_row, axis=0)
            self.rows += 1

    def add_col(self, col: int) -> None:
        if 0 <= col <= self.cols:
            new_col = np.zeros((self.rows, 1), dtype=np.int16)
            self.data = np.insert(self.data, col, new_col, axis=1)
            self.cols += 1