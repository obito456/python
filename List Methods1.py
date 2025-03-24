new=["Batman","Misery"]
shelf.extend(new)
print(shelf)
# Add "The shining" at the front
shelf.insert(0,"The shining")
print(shelf)
#  The last book was teared so remove it
shelf.pop()
print(shelf)
# one wrong genre book needs to be removed
shelf.remove("Batman")
print(shelf)
# place the books in ascending order
shelf.sort()
print(shelf)
# place the books in descending order
shelf.reverse()
print(shelf)
# count the no of "IT" books
print(shelf.count("IT"))
# Make a copy of the shelf
shelf2=shelf.copy()
print(shelf2)
# All books were sold ,make the shelf empty
shelf.clear()
print(shelf) 
