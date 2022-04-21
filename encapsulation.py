
#creating class which will encapsulate the variables which we want protected
#or private
class encapsulate:
    def __init__(self):#instatiating a protected variable
        self._protectedVar = 47#using the protected prefix is a warning with out
        #having to write any comments to let others know not to use outside the class

    def setPrivate(self, private):
        self.__privateVar = private#here we are using the private prefix with the
        #double underscore

    def getPrivate(self):
        print(self.__privateVar)

#even though they are protected or private it doesnt change the behavior as you can still change them
        #but as stated they are just a warning to others that you want this to stay within
        #the class
obj = encapsulate()
print(obj._protectedVar)
obj.setPrivate(666)
obj.getPrivate()
