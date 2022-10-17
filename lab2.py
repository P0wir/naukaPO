from typing import List, Any

# lista: List[int] = [4, 5, -3]
# macierz: List[List[int]] = [[2, 3 ,4], [-3, -8, 5]]
# lista2: List[Any] = [3, "gg"]
#zad 1
X: List[List[int]] = [[2, 3, 4], [-3, -8, 5]]
Y: List[List[int]] = [[4, 6, 8], [-5, -8, 5]]



def matrix_add(X, Y):
    result: List[List[int]] = [0, 0, 0], [0, 0, 0]
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]
    return result

print(matrix_add(X,Y))

X: List[List[float]] = [[2, 3, 4], [-3, -8, 5], [-3, -8, 5]]
Y: List[List[float]] = [[4, 6, 8], [-5, -8, 5], [-3, -8, 5]]
matrix=[]

def multiplicationLineColumn(line,column):
    try:
        sizeLine=len(line)
        sizeColumn=len(column)
        if(sizeLine!=sizeColumn):
            raise ValueError("Exception")
        res = sum([line[i] * column[i] for i in range(sizeLine)])
        return res
    except ValueError:
        print("should have the same len line & column")

def  getColumn(matrix,numColumn):
    size=len(matrix)
    column= [matrix[i][numColumn] for i in range(size)]
    return column

def getLine(matrix,numLine):
    line = matrix[numLine]
    return line

for i in range(len(X)):
    matrix.append([])
    for j in range(len(Y)):
        matrix[i].append(multiplicationLineColumn(getLine(X,i),getColumn(Y,j)))

print(matrix)

dict1 = {'key1': 2, 'key2': 1234, 'key3': 2137, 'key4': 123, 'key5' : 5 }
print(dict1)
print(sorted(dict1))
print(sorted(dict1.items()))
print(sorted(dict1.values()))

dict2 = {'key1': 4, 'key2': 1234, 'key3': 21374, 'key4': 1423, 'key5' : 51 }
dict3 = {}

for key, value in dict2.items():
    dict3[key] = value
for key, value in dict1.items():
    dict3[key] = value

print(dict3)

# initialize tuple
aTuple = (True, 28, 'Tiger')

# tuple to list
aList = list(aTuple)
aList.pop(2)
print(aList)
aaTuple= tuple(aList)
print(aaTuple)

btuple = (1,2,3,4,5,6)
for i in btuple:
    print(btuple[i-1], end = '')
print("")
list1 = [1,2,3,4,5]
list2 = [2,3,4,5,6]
import collections
list3 = list1+list2
print([item for item, count in collections.Counter(list3).items() if count > 1])

listxD = [1,2,3,4,5,6,7]
def liczba_ele(list):
    counter = 0;
    for i in list:
        counter=counter+1
    return counter
print(liczba_ele(listxD))




