# Time complexity: Add - O(1), Get - O(1), Remove - O(1)
# Space complexity: O(n)

class MyHashMap:

    def __init__(self):
        self.hash_map = {}

    def put(self, key: int, value: int) -> None:
        self.hash_map[key] = value

    def get(self, key: int) -> int:
        try:    #if key in self.hash_map:
            return self.hash_map[key]
        except KeyError:    #else:
            return -1

    def remove(self, key: int) -> None:
        try:
            self.hash_map.pop(key)
        except KeyError:
            pass


# MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
