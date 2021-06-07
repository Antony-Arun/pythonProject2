pos = 0
def search(list, n):
    i = 0
    for i in list:
        if i==n:
           globals()['pos']= list.index(i)
           return True, pos
    return False

list  = [5,8,4,6,9,2]

n = int(input("Enter no : "))
if search(list, n):
    print("Found", pos+1)
else:
    print("Not Found")


