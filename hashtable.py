class Hashtable:

    def __init__(self,size=10):
        self.size=size
        self.table=[[] for _ in range(size)]

    def hash_fn(self,key):
        return hash(key)% self.size

    def put(self,key,value):
        index=self.hash_fn(key)

        for item in self.table[index]:
            if item[0]==key:
                item[1]=value

                return

        self.table[index].append([key,value])

    def get(self,key):
        index=self.hash_fn(key)

        for item in self.table[index]:
            if item[0]==key:
                return item[1]

ht=Hashtable()
ht.put("name",'tamilselvi')
ht.put("age",32)
print(ht.get("name"))
print(ht.get("age"))






