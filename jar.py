class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError ("Negative numbers not allowed")

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("exceeds capacity")

        if self.size + n > self.capacity:
            raise ValueError("exceeds capacity")

        self._size += n


    def withdraw(self, n):
        if self.size < n:
            raise ValueError("There are less cookies than asked to remove")

        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar(12)

    jar.deposit(5)

    print(jar)


if __name__ == "__main__":
    main()