class Class1():
    def __init__(self, attr1, attr2, predef_attr = 3, opt_attr = None):
        self.attr1 = attr1
        self.attr2 = attr2
        self.predef_attr = predef_attr
        self.opt_attr = opt_attr

    def meth1(self, param1):
        sum = self.attr1 + self.predef_attr + param1 
        self.attr2 = sum
        print(self.attr2)

class1 = Class1(5,0)
class1.meth1(2)

class Class2(Class1):

    def __init__(self, attr1, attr3):
        # drags the attr1 from the parent and sets attr2 to None
        super().__init__(attr1, None)
        self.attr3 = attr3

    def meth2(self, param2):
        sub = self.attr1 - self.predef_attr - param2
        self.attr3 = sub
        print(self.attr3)

# When calling Class2 now we have to set attr1 and attr3
class2 = Class2(5, 0)
class2.meth2(5)