# type of method 
# instance method
# class method
# static method
# non-member method

class test:
    x1 = 10
    def f1(self):
        print(self.x1)
    @classmethod
    def f2(cls):
        print(cls.x1)
    @staticmethod
    def f3():
        print(test.x1)

def non_member_method():
    print("non member method")

t1 = test()
t1.f1()
t1.f2()
t1.f3()