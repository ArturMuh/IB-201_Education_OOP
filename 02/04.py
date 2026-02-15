class MinStat:
    def __init__(self):
        self.num = []

    def add_number(self, num: int) -> None:
        self.num.append(num)

    def result(self):
        if not self.num:
            return None
        return  min(self.num)

class MaxStat:
    def __init__(self):
        self.num = []

    def add_number(self, num: int) -> None:
        self.num.append(num)

    def result(self):
        if not self.num:
            return None
        return max(self.num)


class AverageStat:
    def __init__(self):
        self.num = []

    def add_number(self, num: int) -> None:
        self.num.append(num)

    def result(self):
        if not self.num:
            return None
        return sum(self.num) / len(self.num)

values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))


mins = MinStat()
maxs = MaxStat()
average = AverageStat()

print(mins.result(), maxs.result(), average.result())

values = [1, 0, 0]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))