class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        output = "🍪" * self.size
        return f"{output}"

    def deposit(self, n):
        if n > (self.capacity - self.size) or n > self.capacity:
            raise ValueError
        else:
            self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

def main():
    x = Jar()
    x.deposit(5)
    print(x)

main()