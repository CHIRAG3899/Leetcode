##Design a HashMap without using any built-in hash table libraries.
##Implement the MyHashMap class:
##MyHashMap() initializes the object with an empty map.
##void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
##int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
##void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 
##Example 1:

##Input
##["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
##[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
##Output
##[null, null, null, 1, -1, null, 1, null, -1]

##Explanation
##MyHashMap myHashMap = new MyHashMap();
##myHashMap.put(1, 1); // The map is now [[1,1]]
##myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
##myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
##myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
##myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
##myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
##myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
##myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size

    def _index(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._index(key)
        if not self.table[idx]:
            self.table[idx] = ListNode(key, value)
            return
        current = self.table[idx]
        while current:
            if current.key == key:
                current.value = value
                return
            if not current.next:
                current.next = ListNode(key, value)
                return
            current = current.next

    def get(self, key: int) -> int:
        idx = self._index(key)
        current = self.table[idx]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        idx = self._index(key)
        current = self.table[idx]
        if not current:
            return
        if current.key == key:
            self.table[idx] = current.next
            return
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next