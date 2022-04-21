from abc import ABC, abstractmethod
#we must import from abc module to use abstraction in our class

class actionSports(ABC):
    def favoriteSport(self, time):#here is our regular method for the class 
        print("Your goal is: ", time)
        @abstractmethod
        def practice(self,time):#this function is asking for the argument but we wont know what kind o fdata it will be
            pass


class skateboardSport(actionSports):#the child class that will define the method from the parent class
    def practice(self, time):#we have defined how to implement the function from the actionSports class 
        print("You practiced for {} and have met and exceeded your goal".format(time))

person1 = skateboardSport()
person1.favoriteSport("2 Hours")
person1.practice("3 Hours")
