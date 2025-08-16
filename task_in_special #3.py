class ShoppingCart:
    def __init__(self,items):
        self.items=items

    def __str__(self):
        return f"Your cart items : {self.items}"

    def __repr__(self):
        return f"ShoppingCart(items {self.items})"

    def __len__(self):
        return len(self.items)

    def __getitem__(self,key):
        return self.items[key]

    def __setitem__(self,key,value):
        self.items[key] = value

item=ShoppingCart(["shampoo","fruits","grenade","flasg boom"])
print(item)
print(repr(item))
print(len(item))

item[3] ="flash grenade"
print(item[3])
