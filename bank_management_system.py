class BankManagementSystem:
    #constructor
    def __init__(self):
        #instance variable
        self.acc_no = None
        self.acc_holder = None
        self.__balance = 0
        
    
    def add_newuser(self, acc_no, acc_holder,amount):
        self.acc_no = acc_no
        self.acc_holder = acc_holder
        self.__balance = amount
        print(f"{acc_holder} has been created successfully!!!")
        
    #Method to check the user balance
    def check_balance(self, acc_no):
        #validate the user
        if acc_no == self.acc_no:
            print(f"The Account holder is {self.acc_holder} balance is {self.__balance}")
        else:
            print("Invalid Account Number!!")
            
    #Method to credit the amount
    def credit_amount(self,acc_no,amount):
        #validate for account number
        if acc_no == self.acc_no:
            self.__balance += amount
            print(f"{amount} has been credited successfully!!!")
        else:
            print("Invalid Acc no")
    
    #Method for withdraw the amount
    def withdraw_amount(self,acc_no,amount):
        #validate acc no
        if acc_no == self.acc_no:
            #handle insufficient balance
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"{amount} has been withdraw successfully!!")
            else:
                print("Insufficient Balance!!")
        else:
            print(f"Invalid acc no")
            
    #Method to Update the user
    def update_user(self,acc_no,new_acc_holder):
        if acc_no == self.acc_no:
            self.acc_holder = new_acc_holder
            print(f"{new_acc_holder} has been updated successfully!!!")
        else:
            print("Invalid acc no")
u1 = BankManagementSystem()
u1.add_newuser("SBI01",'saniya',2000)
u1.check_balance("SBI01")
u1.credit_amount("SBI01",500)
u1.check_balance("SBI01")
u1.withdraw_amount("SBI01",1500)
u1.check_balance("SBI01")

u1.update_user("SBI01","Syeda Saniya")
u1.check_balance("SBI01")

u2 = BankManagementSystem()
u2.add_newuser("SBI02","Gulfam",3000)
u2.check_balance("SBI02")
