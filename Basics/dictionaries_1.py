dist = {'Jack':15,'Bob':20,'Alice':19}

print(dist)

print(dist['Jack'])

'''add dist'''

dist['joan']=14

print(dist)

'''Overwrite dist'''

dist['joan']=15

print(dist)

'''delete in dist'''

del dist['joan']

print(dist)

for i in dist.items():
    #k,v=i
    print(i)
