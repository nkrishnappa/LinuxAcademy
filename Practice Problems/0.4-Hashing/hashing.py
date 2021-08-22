HASH_MAX_SIZE = 100

class HashTable:
    def __init__(self) -> None:
        self.MAX = HASH_MAX_SIZE
        self.array= [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            # Return the Unicode code point for a one-character string.
            h += ord(char)
        return h % self.MAX

    # def add(self, key, value):
    def __setitem__(self, key, value):
        index = self.get_hash(key)
        # print(index)
        self.array[index] = value

    # def get(self, key):
    def __getitem__(self, key):
        index = self.get_hash(key)
        return self.array[index]
    
    def __delitem__(self, key):
        index = self.get_hash(key)
        self.array[index] = None


if __name__ == "__main__":
    hash = HashTable()

    # outputs are with HASH_MAX_SIZE = 100
    
    # print(hash.get_hash("Nandisha")) # 6
    # print(hash.get_hash("11-Mar")) # 31

    '''
    hash.add("11-Mar", 323.0)
    print(f"The stock price on 11-Mar was : {hash.get('11-Mar')}")
    # The stock price on 11-Mar was : 323.0
    '''

    '''
    hash["11-Mar"] = 323.0
    print(f"The stock price on 11-Mar was : {hash['11-Mar']}")
    # The stock price on 11-Mar was : 323.0
    '''

    hash["7-Mar"] = 340.0
    hash["8-Mar"] = 380.0 
    hash["9-Mar"] = 302.0
    hash["10-Mar"] = 297.0
    hash["11-Mar"] = 323.0

    print(hash.array)
    print(f"The stock price on 11-Mar was : {hash['11-Mar']}")
    """
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 297.0, 323.0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 340.0, 380.0, 302.0, None, None, None, None, None, None, None, None, None]
    """
    # hash.__delitem__('11-Mar')
    del hash['11-Mar']
    print(hash.array)
    print(f"The stock price on 11-Mar was : {hash['11-Mar']}")
    """
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 297.0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 340.0, 380.0, 302.0, None, None, None, None, None, None, None, None, None]
    The stock price on 11-Mar was : None
    """