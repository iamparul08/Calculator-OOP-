#calculator using the OOP concept

import sys
#-------------------------------------------Business Logic Layer
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

#---------------------------------------------Presentation Layer

obj = calculator()
while True:
    print("\n Calculator")
    print("\n 1. ADD \n 2. SUBSTRACTION \n 3. MULTIPLY \n 4. DIVISION \n 5. POWER \n 6. EXIT")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.no1 = int(input("Enter number 1: "))
        obj.no2 = int(input("Enter number 2: "))
        obj.sum()
        print("Result = ", obj.res)
    
    elif choice == 2:
        obj.no1 = int(input("Enter number 1: "))
        obj.no2 = int(input("Enter number 2: "))
        obj.substraction()
        print("Result = ", obj.res)
    
    elif choice == 3:
        obj.no1 = int(input("Enter number 1: "))
        obj.no2 = int(input("Enter number 2: "))
        obj.multiplication()
        print("Result = ", obj.res)
    
    elif choice == 4:
        obj.no1 = int(input("Enter number 1: "))
        obj.no2 = int(input("Enter number 2: "))
        obj.division()
        print("Result = ", obj.res)
    
    elif choice == 5:
        obj.no1 = int(input("Enter number 1: "))
        obj.no2 = int(input("Enter number 2: "))
        obj.power()
        print("Result = ", obj.res)
        
    elif choice == 6:
        print("Exit successfully")
        sys.exit()
    
    else:
        print("Invalid Choice")
