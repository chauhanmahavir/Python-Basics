class MyClass:
    def instancemethod(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

obj=MyClass()
print(MyClass.classmethod())
print(MyClass.staticmethod())
print(MyClass.instancemethod(obj))

'''print(obj.instancemethod())'''
