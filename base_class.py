class mathematics:
    def __init__(self):
        self.exists = True

    def add(self, num1, num2):
        if num1.isdigit() and num2.isdigit():
            return(float(num1) + float(num2))
        else:
            print("please type valid numbers")

    def subtract(self, num1, num2):
        if num1.isdigit() and num2.isdigit():
            return(float(num1) - float(num2))
        else:
            print("please type valid numbers")

    def multiply(self, num1, num2):
        if num1.isdigit() and num2.isdigit():
            return(float(num1) * float(num2))
        else:
            print("please type valid numbers")

    def divide(self, num1, num2):
        if num1.isdigit() and num2.isdigit():
            return(float(num1) / float(num2))
        else:
            print("please type valid numbers")

    def CMtoM(self, num1):
        if self.isdigit():
            return((float(num1))/100)
        else:
            print("please type valid numbers")

    def MtoFEET(self, num1):
        if num1.isdigit():
            return(round(((float(num1))*3.2808399),2))
        else:
            print("please type valid numbers")
class calculator(mathematics):
    def __init__(self):
        super().__init__()

    def calculator(self):
        calculate = True
        while calculate:
            button = input("press calculator button here (+,-,*,/,(CM for m from cm),(F for feet from m),(x for exit)):")
            if button == "-":
                print (mathematics.subtract(self, num1=input("first number:"), num2=input("second number:")))
            elif button == "+":
                print (mathematics.add(self, num1=input("first number:"),num2=input("second number:")))
            elif button == "*":
                print (mathematics.multiply(self, num1=input("first number:"),num2=input("second number:")))
            elif button == "/":
                print (mathematics.divide(self, num1=input("first number:"),num2=input("second number:")))
            elif button.upper() == "CM":
                print (mathematics.CMtoM(self, num1 = input("number of cm:")))
            elif button.upper() == "F":
                print (mathematics.MtoFEET(self, num1 = input("number of m:")))

            elif button == "x":
                print ("exiting ...")
                calculate = False
            else:
                print("not a button")