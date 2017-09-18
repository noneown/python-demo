from random import randint

class Dbox():
    def __init__(self, num_sizes, num_ds):
        self.num_sizes = num_sizes
        self.num_ds = num_ds

    def roll(self):
        result = 0
        for i in range(0, self.num_ds):
            result += randint(1, self.num_sizes)
        return result

    def get_avalible_sum(self, lista, listb):
        result = []
        for i in lista:
            for j in listb:
                result.append(i + j)

        return list(set(result))

    def get_all_num(self):
        if self.num_ds == 1:
            return range(1, self.num_sizes + 1)

        result = self.get_avalible_sum(range(1, self.num_sizes + 1), range(1, self.num_sizes + 1))
        for i in range(self.num_ds - 2):
            result = self.get_avalible_sum(result, range(1, self.num_sizes + 1))

        return  result