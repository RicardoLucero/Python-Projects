

#parent class
class Footware:
    make = 'Converse'
    model = 'chucks'
    color = 'black'

    def myShoes(self):
        msg = "My shoes are {} {} {}".format(self.color,self.model,self.make)
        return msg
        

#child class boots
class Boots(Footware):
    make =  'timberlands'
    model = 'timbs'
    color = 'brown'
    toecap = 'steel toe'
    waterproof = True

#same method as the parent class except we are making it about the boots
    def myShoes(self):
        msg = '\nMy {} are {}\nthey are safe for work\nthey are {}s'.format(self.make,self.color,self.toecap)
        return msg

#Another child class
class Runners(Footware):
    make = 'Nike'
    model = 'air maxxx'
    color = 'neon green'
    heel = 'air pocket'
    insole = 'runners bounce'

#once again the same method but about the running shoes
    def myShoes(self):
        msg = '\nMy {} {}\nare {} they have an {}\nso they help when running\nto not tire your feet out so much'.format(self.make,self.model,self.color,self.heel)
        return msg

if __name__ == '__main__':
    shoes = Footware()
    print(shoes.myShoes())

    boots = Boots()
    print(boots.myShoes())

    run = Runners()
    print(run.myShoes())

