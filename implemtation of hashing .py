class HashTable:
    def __init__(self):
        self.data = {}

    # create / insert
    def insert(self, key, value):
        self.data[key] = value

    # get
    def get(self, key):
        return self.data.get(key)

    # default
    def default(self, key, value):
        return self.data.get(key, value)

    # exists
    def exists(self, key):
        return key in self.data

    # remove
    def remove(self, key):
        self.data.pop(key, None)

    # size
    def size(self):
        return len(self.data)

    # keys
    def keys(self):
        return list(self.data.keys())

    # values
    def values(self):
        return list(self.data.values())

    # entries
    def entries(self):
        return list(self.data.items())

    # clear
    def clear(self):
        self.data.clear()
    # Example
h = HashTable()

h.insert("name", "Arpita")
h.insert("age", 20)

print(h.get("name"))
print(h.default("city", "Delhi"))
print(h.exists("age"))
print(h.size())
print(h.keys())
print(h.values())
print(h.entries())

h.remove("age")
print(h.entries())

h.clear()
print(h.size())


