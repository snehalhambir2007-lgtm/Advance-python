class Numbers:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= self.limit:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration


# Main Program
limit = int(input("Enter the last number: "))

numbers = Numbers(limit)

print("Numbers are:")
for i in numbers:
    print(i)
