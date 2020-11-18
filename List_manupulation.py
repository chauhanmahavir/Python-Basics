x = [2,3,5,2,4,6,4]

'''Apend at last position
append(value)'''
x.append(2)
print(x)

'''Insert(index,value)'''
x.insert(2,99)
print(x)

'''remove(value)
remove first value)'''
x.remove(2)
print(x)


'''remove at inddex 2'''
x.remove(x[2])
print(x)

'''print(x[start:stop])
It will print form start index to stop-1 index'''
print(x[3:6])


'''print last element of list'''
print(x[-1])


'''print last second element of list'''
print(x[-2])


'''print index of value
print index of value 4'''
print(x.index(4))

'''count the spacific value in list'''
print(x.count(4))

'''sort the element of list'''
x.sort()
print(x)

y=['Jan','jone','bob','jan']
y.sort()
print(y)
