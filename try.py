

def guessInfo():
    var1 = input("Please provide your begining value")
    var2 = input("Please provide your ending value")
    guesser(var1,var2)



def guesser(var1,var2):
    try:
        var3 = int(var1) - int(var2)
        print("{} - {} is your number = {}".format(var1,var2,var3))
    except:
        print("The Values need to be numeric!")




if __name__ == "__main__":
    guessInfo()
