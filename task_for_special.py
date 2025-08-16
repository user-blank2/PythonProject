class story:
    def __init__(self,title,author):
        self.title = title
        self.author= author

    def __str__(self):
        return f"Book {self.title} : {self.author} "

    def __repr__(self):
        return  f"Title = <{self.title}> , author = '<{self.author}'>"

my_story = story("LIFE","MR FOOL")
print(my_story)
print(repr(my_story))