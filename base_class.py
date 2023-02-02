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

