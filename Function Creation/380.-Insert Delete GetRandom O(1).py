import random


class RandomizedSet:

    def __init__(self):
        self.hashmap = {}

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            self.hashmap.pop(val)
            return True

    def getRandom(self) -> int:
        lst = list(self.hashmap.keys())
        x = random.choice(lst)
        return x


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
