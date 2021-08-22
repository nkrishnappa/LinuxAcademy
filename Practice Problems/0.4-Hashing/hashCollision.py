class HashTable:
    def __init__(self) -> None:
        self.MAX = HASH_MAX_SIZE
        #self.array= [None for i in range(self.MAX)]
        self.array= [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            # Return the Unicode code point for a one-character string.
            h += ord(char)
        return h % self.MAX

    # def add(self, key, value):
    def __setitem__(self, key, value):
        index = self.get_hash(key)
        print(f"key[{index}]: {key:7} {self.array[index]}")
        
        # self.array[index] = value # 🐛
        # To avoid the collition we are using the tuple of elements
        found = False

        # To avoid duplicate - [('9-Mar', 302.0), ('9-Mar', 310.0)]  
        for item_index, element in enumerate(self.array[index]):
            # print(item_index, element) # 0 ('9-Mar', 302.0)
            # print(index, key,value)    # 0 10-Mar 297.0
            if len(element) == 2 and element[0] == key:
                self.array[index][item_index] = (key, value)
                found = True
                break
        if not found:
            self.array[index].append((key, value))
        
    # def get(self, key):
    def __getitem__(self, key):
        index = self.get_hash(key)
        # print(f"key[{index}]: {key:7} {self.array[index]}")
        for element in self.array[index]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        index = self.get_hash(key)
        for item_index, element in enumerate(self.array[index]):
            if element[0] == key:
                del self.array[index][item_index]
        # self.array[index] = None

# Linear Probing - Searching next empty slot to store the element
HASH_MAX_SIZE = 10

hash = HashTable()
hash["7-Mar"] = 340.0
hash["8-Mar"] = 380.0 
hash["9-Mar"] = 302.0  # 🐛
hash["9-Mar"] = 310.0  # 🐛
hash["10-Mar"] = 297.0 # 🐛
hash["11-Mar"] = 323.0

print(hash.array)
print(f"The stock price on 9-Mar was  : {hash['9-Mar']:5}")
print(f"The stock price on 10-Mar was : {hash['10-Mar']:5}")
print(f"The stock price on 11-Mar was : {hash['11-Mar']:5}")

del hash["10-Mar"]
print(hash.array)
print(f"The stock price on 10-Mar was : {hash['10-Mar']}")
"""
Final Output:
key[8]: 7-Mar   []
key[9]: 8-Mar   []
key[0]: 9-Mar   []
key[0]: 10-Mar  [('9-Mar', 302.0)]
key[1]: 11-Mar  []
[[('9-Mar', 302.0), ('10-Mar', 297.0)], [('11-Mar', 323.0)], [], [], [], [], [], [], [('7-Mar', 340.0)], [('8-Mar', 380.0)]]
323.0
The stock price on 9-Mar was  : 302.0
The stock price on 10-Mar was : 297.0
The stock price on 11-Mar was : 323.0
[[('9-Mar', 302.0)], [('11-Mar', 323.0)], [], [], [], [], [], [], [('7-Mar', 340.0)], [('8-Mar', 380.0)]]
The stock price on 10-Mar was : None
"""


"""
Where is 9-Mar : 302.0 ? 

key[8]: 7-Mar   []
key[9]: 8-Mar   []
key[0]: 9-Mar   []
key[0]: 10-Mar  302.0
key[1]: 11-Mar  []
[297.0, 323.0, [], [], [], [], [], [], 340.0, 380.0]

"""

"""
After introducing the tuple of elements if the key matching

key[8]: 7-Mar   []
key[9]: 8-Mar   []
key[0]: 9-Mar   []
key[0]: 10-Mar  [('9-Mar', 302.0)]
key[1]: 11-Mar  []
[[('9-Mar', 302.0), ('10-Mar', 297.0)], [('11-Mar', 323.0)], [], [], [], [], [], [], [('7-Mar', 340.0)], [('8-Mar', 380.0)]]

"""

