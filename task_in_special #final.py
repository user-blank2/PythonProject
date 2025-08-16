class LibraryShelf:
    def __init__(self,book):
        self.book=book

    def __str__(self):
        return f"Your book list : {self.book}"

    def __repr__(self):
        return f"LibraryShelf(book={self.book})"

    def __len__(self):
        return len(self.book)

    def __getitem__(self,key):
        return self.book[key]

    def __setitem__(self,key,value):
        self.book[key] =value

    def __contains__(self,key):
        return key in self.book

    def __eq__(self,other):
        return self.book == other.book


shelf1 = LibraryShelf(["AI","Machine learning","Robotics"])
shelf2 = LibraryShelf(["Maths","English","Robotics"])

print(shelf1)
print(shelf2)

print(shelf1[0])

shelf1[0]="DS"
print(shelf1)

print("Maths" in shelf2)

print(len(shelf2))

for book in shelf1:
    print(book)

print(shelf1[2] == shelf2[2])







