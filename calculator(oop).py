#calculator using the OOP concept

import sys
#-------------------------------------------BLL
class calculator:
    def __init__(self):
        self.no1 = 0
        self.no2 = 0
        self.res = 0
    def sum(self):
        self.res = self.no1 + self.no2
    def substraction(self):
        self.res = self.no1 - self.no2
    def multiplication(self):
        self.res = self.no1 * self.no2
    def division(self):
        self.res = self.no1 / self.no2
    def power(self):
        self.res = self.no1 ** self.no2

#---------------------------------------------PL

obj = calculator()
while True:
    print("\n Calculator")
    print("\n 1. ADD \n 2. SUBSTRACTION \n 3. MULTIPLY \n 4. DIVISION \n 5. POWER \n 6. EXIT")
    p = int(input("Enter your choice: "))

    if p != 6:
        obj.no1 = int(input("Enter number 1: "))
        obj.no2 = int(input("Enter number 2: "))
    if p == 1:
        obj.sum()
        print("Result = ", obj.res)
    elif p ==2:
        obj.substraction()
        print("Result = ", obj.res)
    elif p ==3:
        obj.multiplication()
        print("Result = ", obj.res)
    elif p==4:
        obj.division()
        print("Result = ", obj.res)
    elif p==5:
        obj.power()
        print("Result = ", obj.res)
    else:
        print("Exit successfully")
        sys.exit()
