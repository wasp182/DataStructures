class HashTable:
    def __init__(self):
        # based on load factor we may change the size of underlying DS
        self.capacity = 10
        self.keys = [None]*self.capacity
        self.values = [None]*self.capacity

    def hash_function(self,key):
        hash_sum = 0
        for letters in key:
            hash_sum += ord(letters)
        # ord function will transform keys into ASCII nos

        return hash_sum%self.capacity

    def insert(self,key,data):
        # find valid location for value
        index = self.hash_function(key)
        while self.keys[index] :
            # if key is already present , update the value
            if self.keys[index] == key :
                self.values[index] = data
                return
            # linear probing modulo capc to ensure no out of bounds occur
            index = (index+1)% self.capacity
        # valid index for data found
        self.keys[index]=key
        self.values[index] = data

    def get(self,key):
        # find the valid location
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = ( index+1 ) % self.capacity
        return None





if __name__ =="__main__":
    table = HashTable()
    print(table.hash_function("hashable"))
    table.insert("Adam",32)
    table.insert("Kevin",22)
    table.insert("Dan",42)
    print(table.get("Adam"))