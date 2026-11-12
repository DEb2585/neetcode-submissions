class MyHashSet:
    def __init__(self):
        self.data = [False] * (10**6 + 1)   # one slot per possible key

    def add(self, key: int) -> None:
        self.data[key] = True               # mark key as present

    def remove(self, key: int) -> None:
        self.data[key] = False              # mark key as absent

    def contains(self, key: int) -> bool:
        return self.data[key]               # True if present
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)