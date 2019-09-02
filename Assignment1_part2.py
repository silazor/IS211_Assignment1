#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Book:
    def __init__(self, title, author):
        self.author = author
        self.title = title
    def display(self):
        print(self.title, "written by " + self.author)

book1 = Book("Of Mice and Men", "John Steinbeck")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

book1.display()
book2.display()

