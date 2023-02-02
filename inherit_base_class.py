from base_class import mathematics

class calculator(mathematics):
    def __init__(self):
        super().__init__()


    def calculator(self):
        calculate = True
        while calculate:
            button = input("press calculator button here (+,-,*,/,(CM for m from cm),(F for feet from m),(x for exit)):")
            if button == "-":
                print (mathematics.subtract(self, num1=input("first number:"),num2=input("second number:")))
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

math = calculator()
math.calculator()