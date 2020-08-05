from statistics import variance
example_list=[10,20,30,40,50,60,70,80,90,100]
x=variance(example_list)

print(x)

print('New Method')

from statistics import variance as v
example_list=[10,20,30,40,50,60,70,80,90,100]
x=v(example_list)

print(x)

print('new method')

from statistics import variance,mean
example_list=[10,20,30,40,50,60,70,80,90,100]
x=variance(example_list)
y=mean(example_list)
print(x)
print(y)

print('new method')

from statistics import variance as v,mean as m
example_list=[10,20,30,40,50,60,70,80,90,100]
x=v(example_list)
y=m(example_list)
print(x)
print(y)


''' from statistics import *'''
'''That means all function are included'''
