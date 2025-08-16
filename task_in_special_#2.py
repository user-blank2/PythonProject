class Notebook:
    def __init__(self,books):
        self.books=books

    def __str__(self):
        return f"NoteBook : {self.books}"

    def __repr__(self):
        return f"NoteBook ({self.books})"

    def __len__(self):
        return len(self.books)

    def __getitem__(self,key):
        return self.books[key]

    def __setitem__(self,key,value):
        self.books[key]  = value

notes=Notebook(["japanese", "python","English","AI"])

print(notes)
print(repr(notes))
print(len(notes))
print(notes[0])
notes[2] = "Maths"
print(notes[2])



