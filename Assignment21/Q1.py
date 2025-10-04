#Develop a simple calculator program that perform basic arithmatic operations on the two number given by user
import exceptionClass as ex

if __name__ == "__main__":
    ch = 0
    while(ch != True):
        try:
            def add(a,b):
                return a + b
            
            def sub(a,b):
                return a - b
            
            def mul(a,b):
                return a * b
            
            def div(a,b):
                return a / b
            
            print("\n+ for Additon")
            print("- for Subtraction")
            print("* for Multification")
            print("/ for Division")
            ch = input("Enter choice: ")
            a = int(input("Enter number: "))
            b = int(input("Enter number: "))

            if ch == "+":
                print(add(a,b))
            elif ch == "-":
                print(sub(a,b))
            elif ch == "*":
                print(mul(a,b))
            elif ch == "/":
                print(div(a,b))
            else:
                raise ex.InvalidOperator()
            
        except ZeroDivisionError:
            print("Denominator will not be zero")

        except ex.InvalidOperator:
            print("Please Enter Correct Operator")

        except ValueError:
            print("Enter Numeric value")

        except:
            print("Try Again ")

               
    
            
