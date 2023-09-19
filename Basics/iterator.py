a = ["Hello", "World"]

# This for loop is basically use the iter build in function to go to next element. 

for i in a:
    print(i)

# We can build by our own 

itr = iter(a)

print(itr)

print(next(itr))

print(next(itr))

# Below command gives the stop iterator error because there is not other elements.
# print(next(itr))

# There is also one more function for the reverse iterator "reversed"

# This will print the list in reverse order.
rev_itr = reversed(a)

print(next(rev_itr))

print(next(rev_itr))

class RemoteControl():
    def __init__(self):
        self.channels = ["HBO","cnn","abc","espn"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration

        return self.channels[self.index]

r = RemoteControl()
itr=iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))