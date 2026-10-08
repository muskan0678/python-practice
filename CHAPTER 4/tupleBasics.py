# tuples Basics

myTuple= (78, 90, 75)
studentTuple= ("Khushi", "Divya", "Ishaan", "Mussu")

# studentTuple[1]= "Anchal" Tuples are IMMUTABLE/NOT Changeable

print(studentTuple[2])

# empty Tuples
emptyTuple= ()
singleTuple= (1,)
print(type(emptyTuple))
print(type(singleTuple))
print(studentTuple.index("Mussu"))
print(studentTuple.count("Khushi"))