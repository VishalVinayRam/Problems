class DynamicArray:
    
    def __init__(self, capacity: int):
        self.l = []
        self.max_capacity= capacity
        self.current_capacity = 0

    def get(self, i: int) -> int:
        return self.l[i]

    def set(self, i: int, n: int) -> None:
        if self.current_capacity == 0:
            return 
        self.l[i] = n
        return

    def pushback(self, n: int) -> None:
        print(f'{self.l} pushing back at position {len(self.l)}')
        if self.max_capacity == self.current_capacity:
            self.resize()
        self.current_capacity +=1
        self.l.append(n)
        return

    def popback(self) -> int:
        if self.current_capacity == 0:
            return
        self.current_capacity-=1
        return self.l.pop()

    def resize(self) -> None:
        print(f'max capacity is {self.max_capacity}')
        self.max_capacity = self.max_capacity*2

    def getSize(self) -> int:
        return self.current_capacity
    
    def getCapacity(self) -> int:
        print(f'max capacity is {self.max_capacity}')
        return self.max_capacity
