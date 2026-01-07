class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers


    def __iter__(self):
        self.index = 0
        return self


    def __next__(self):
        if self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            return value
        raise StopIteration




if __name__ == "__main__":
    nums = Numbers([1, 2, 3])
    for n in nums:
        print(n)