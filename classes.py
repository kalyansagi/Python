# Example file for working with classes

class myClass():
    def method1(self):
        print("my class method1")
    def method2(self, someString):
        print("myclass method2 " + someString)

class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")
    def method2(self, someString):
        print("anotherClass method2 " + someString)


def main():
    c = myClass()
    c.method1()
    c.method2("This is a String")

    c2 = anotherClass()
    c2.method1()
    c2.method2("This is a String")



main()