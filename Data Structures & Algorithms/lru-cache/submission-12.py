class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap = {}
        self.cap = capacity
        self.left, self.right = Node(None, None), Node(None, None)
        self.left.next, self.right.prev = self.right, self.left
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    def insert(self, node):
        node.prev, node.next = self.right.prev,self.right
        self.right.prev.next, self.right.prev = node, node

    def get(self, key: int) -> int:
        if key in self.hashMap:
            retNode = self.hashMap[key]
            self.remove(retNode)
            self.insert(retNode)
            return retNode.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
        node = Node(key, value)
        self.hashMap[key] = node
        self.insert(node)

        if len(self.hashMap) > self.cap:
            tmp = self.left.next
            self.remove(self.left.next)
            self.hashMap.pop(tmp.key)

