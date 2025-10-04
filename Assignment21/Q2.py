import exceptionClass as ex
class Television:
    
    def __init__(self,model_no=0,screen_size=0,price=0):
        self.model_no = model_no
        self.screen_size = screen_size
        self.price = price

    def reset(self):
        self.model_no = 0
        self.screen_size = 0
        self.price = 0

    def userInput(self):
        try:
            self.model_no = int(input("Enter Model number: "))
            if self.model_no > 9999:
                raise ex.numberOverload()

            self.screen_size = int(input("Enter Screen Size (inches): "))
            if self.screen_size < 12:
                raise ex.smallSize()
            elif self.screen_size > 70:
                raise ex.overSize()

            self.price = int(input("Enter Price: "))
            if self.price > 5000:
                raise ex.overPrice()
            elif self.price < 0:
                raise ex.negitivePrice()
            
        except ex.numberOverload:
            print("Model number is more than 4 digits")
            self.reset()

        except ex.smallSize:
            print("Screen Size is Small")
            self.reset()

        except ex.overSize:
            print("Size is Greater than 70 inches")
            self.reset()

        except ex.overPrice:
            print('Price is Greater than 5000Rs')
            self.reset()

        except ex.negitivePrice:
            print('Price is not negitive')
            self.reset()

    def __str__(self):
        return  f"Model Number:{self.model_no}, Screen Size:{self.screen_size}, Price:{self.price}"

    
    def display(self):
        print(self.__str__())
        
    

if __name__ == "__main__":
    try:
        t = Television()
        print("1.Enter Data ")
        print("2.Display Data")
        ch = int(input("Enter Choice: "))
        if ch == 1:
            t.userInput()
        elif ch == 2:
            t.display()
        else:
            print('Enter Correct choice')

    except ValueError:
        print("Enter numeric value")
    


