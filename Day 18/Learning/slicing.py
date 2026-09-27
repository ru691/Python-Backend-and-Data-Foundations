piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
           # [ 1 ,  2,   3,   4,   5,   6,   7 ]
print(piano_keys[2:5]) #TAKE ANYTHING AFTER 2 TILL 5
print(piano_keys[2:]) #TAKE ANYTHING AFTER 2 TILL END OF THE LIST
print(piano_keys[:5]) #TAKE FROM THE BEGINNING TILL POSITION 5
print(piano_keys[2:5:2]) #TAKE FROM 2 TILL 5, THIRD NUMBER AFTER : MEANS
                         #IN THE LIST PRINT INCREMENT OF 2 EG. 1,3,5,7
print(piano_keys[::2]) #print everything in the list but increment of 2
print(piano_keys[::-1])#print list in reverse, 1 by 1

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
print(piano_tuple[2:5])