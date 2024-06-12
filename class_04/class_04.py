from typing import Any
myList : list[Any] = ["qasim","Naveed Sarwar","ali"]
print(myList)
print(myList[2].upper())
print(f'founder of techloset solution {myList[1].title()}')

# slicing
character : list[str] = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g' ]
print( character[1::2] )  

# looping through slicing
print("Here are the first three characters of my list:")
for  char in character[:3]:    
    print(char)  