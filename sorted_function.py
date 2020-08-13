#sorted(iterable, key=key, reverse=reverse) 

# List 
x = ['q', 'w', 'r', 'e', 't', 'y'] 
print (sorted(x)) 
  
# Tuple 
x = ('q', 'w', 'e', 'r', 't', 'y') 
print (sorted(x)) 
  
# String-sorted based on ASCII translations 
x = "python"
print (sorted(x)) 
  
# Dictionary 
x = {'q':1, 'w':2, 'e':3, 'r':4, 't':5, 'y':6} 
print (sorted(x)) 
  
# Set 
x = {'q', 'w', 'e', 'r', 't', 'y'} 
print (sorted(x)) 
  
# Frozen Set 
x = frozenset(('q', 'w', 'e', 'r', 't', 'y')) 
print (sorted(x)) 

# Using Key Parameter

L = ["cccc", "b", "dd", "aaa"]
print ("Normal sort :", sorted(L))   
print ("Sort with len :", sorted(L, key = len)) 

# Sort a list of integers based on 
# their remainder on dividing from 7

def func(x): 
	return x % 7
L = [15, 3, 11, 7] 
print ("Normal sort :", sorted(L)) 
print ("Sorted with key:", sorted(L, key = func)) 

