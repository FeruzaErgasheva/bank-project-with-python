from datetime import datetime
class InputError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
class InsufficeintMOney(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Bank:
    all=[]
    def __init__(self,name,comission,money) -> None:
        self.name=name
        self.comission=comission
        self.__money=money
        
        Bank.all.append(self)
    
    

class BankAccount:
    def __init__(self,name,id,password,phnumber:str,balance:float,paymentHistory=[]) -> None:
        self.__name=name
        self.__id=id
        self._password=password
        self.__phnumber=phnumber
        self.__balance=balance
        self.__paymentHistory=[]
        
    def getAccountInfo(self):
        return f"""
    name:{self.__name}
    id:{self.__id}
    phnumber={self.__phnumber}
    balance={self.__balance}
    """
    
    def getId(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @property
    def phnumber(self):
        return self.__phnumber
    @property
    def getBalance(self):
        return self.__balance
    def getPaymentHistory(self):
        return self.__paymentHistory    
    def recordPayment(self,userName:str,time:str,toPerson:str,money:float):
        paymentInfo={
            "Card owner name":userName,
            "time":time,
            "Transfered person name":toPerson,
            "money":money,
            "Current balance":self.__balance
        }
        self.__paymentHistory.append(paymentInfo)
    
    @name.setter
    def nameSetter(self,newName):
        if isinstance(newName,str):
            self.__name=newName
        else:
            raise InputError
        
    @phnumber.setter
    def phnumberSetter(self,newNumber:str):
        if newNumber.startswith("99899")  or newNumber.startswith("99897") or newNumber.startswith("99890"):
            self.__phnumber=newNumber
        else:
            raise InputError
    #payment history
    def addBalance(self,amount:float):
        if amount>0:
            self.__balance+=amount
            currentTime=datetime.now().strftime("%H:%M:%S")
            toPerson=self.__name
            self.recordPayment(self.__name,currentTime,toPerson,amount)
            
        else:
            raise InputError
    #paymenthistory
    def withdraw(self,money):
        if self.__balance-money<0:
            raise  InsufficeintMOney
        else:
            self.__balance-=money
            currentTime=datetime.now().strftime("%H:%M:%S")
            self.recordPayment(self.__name,currentTime,self.__name,money)
            
    #payment history
    def transfer(self,toAccount:object,transferMoney:float,comission):
        totalMoney=(transferMoney+transferMoney*comission)
        if self.__balance-totalMoney>=0:
            self.__balance-=totalMoney
            toAccount.__balance+=transferMoney
            currentTime=datetime.now().strftime("%H:%M:%S")
            self.recordPayment(self.__name,currentTime,toAccount.__name,transferMoney)
            toAccount.recordPayment(toAccount.__name,currentTime,self.__name,transferMoney)
        else:
            raise InsufficeintMOney
        
        
user1=BankAccount("Feruza","03015","Sumayya_0406","998993030917",200_000)
user2=BankAccount("Fayoza","03255","777777","998908191104",0)
user1.transfer(user2,10000,0.01)
print(user1.getPaymentHistory())
print(user2.getPaymentHistory())


            

        
    
   
        
       