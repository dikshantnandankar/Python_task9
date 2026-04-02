class Bank:
    def __init__(self,bname,bid,bBranch):
        self.bank_name = bname
        self.bank_id = bid
        self.bank_Branch = bBranch

    def bankdetails(self):
        return {
            'bank_name' : self.bank_name,
            'bank_id' : self.bank_id,
            'bank_Branch' : self.bank_Branch
        }
    
# b1 = Bank('bank1',101,'Nagpur')
# bank1 = b1.bankdetails()
# print('bank1' , bank1)
    
class Customer:
    def __init__(self,cname,cacc_no,cacc_type,cbalance,copen_date):
        self.cust_name = cname
        self.cust_acc_no = cacc_no
        self.cust_acc_type = cacc_type
        self.cust_balance = cbalance
        self.cust_acc_open_date = copen_date

    def custdetails(self):
        return {
            'cust_name' : self.cust_name,
            'cust_acc_no' : self.cust_acc_no,
            'cust_acc_type' : self.cust_acc_type,
            'cust_balance' : self.cust_balance,
            'cust_acc_open_date' : self.cust_acc_open_date
        }
    
# c1 = Customer('Happy',123456789,'Savings',50000,'20-3-2026')
# customer1 = c1.custdetails()
# print('customer1', customer1)
    
class Transaction(Bank,Customer):
    def __init__(self, transdetails):
        super().__init__(transdetails.get('bank_name'),transdetails.get('bank_id'),transdetails.get('bank_Branch'))
        Customer.__init__(self,transdetails.get('cust_name'),transdetails.get('cust_acc_no'),transdetails.get('cust_acc_type'),
                          transdetails.get('cust_balance'),transdetails.get('cust_acc_open_date'))
        
    def deposit(self,amount):
        self.cust_balance = self.cust_balance + amount
        print(f'customer account no {self.cust_acc_no} deposited {amount} successfully, New_balance : {self.cust_balance}')
        return {'cust_balance' : self.cust_balance}

    def withdraw(self,amt):
        if amt <= self.cust_balance :
            self.cust_balance = self.cust_balance - amt
            print(f'Amount {amt} is withdrawn from account no {self.cust_acc_no} and current balance : {self.cust_balance}')
            return {'cust_balance' : self.cust_balance}
        else:
            print('Insuffcient balance')
            return {'cust_balance' : self.cust_balance}

    def gettransdetails(self):
        getbankdetails = self.bankdetails()
        getcustdetails = self.custdetails()
        print('This is customer account details')
        return {
            'bank_name' : getbankdetails.get('bank_name'),
            'bank_id' : getbankdetails.get('bank_id'),
            'bank_Branch' : getbankdetails.get('bank_Branch'),
            'cust_name' : getcustdetails.get('cust_name'),
            'cust_acc_no' : getcustdetails.get('cust_acc_no'),
            'cust_acc_type' : getcustdetails.get('cust_acc_type'),
            'cust_balance' : getcustdetails.get('cust_balance'),
            'cust_acc_open_date' : getcustdetails.get('cust_acc_open_date')
        }
t1details = [{
    'bank_name' : 'SBI',
    'bank_id' : 'SBI101',
    'bank_Branch' : 'Nagpur',
    'cust_name' : 'Happy',
    'cust_acc_no' : 123456789,
    'cust_acc_type' : 'Savings',
    'cust_balance' : 50000,
    'cust_acc_open_date' : '20-3-2026'
},
{
    'bank_name' : 'PNB',
    'bank_id' : 'PNB101',
    'bank_Branch' : 'Mumbai',
    'cust_name' : 'Ajay',
    'cust_acc_no' : 1500000987,
    'cust_acc_type' : 'Current',
    'cust_balance' : 500000,
    'cust_acc_open_date' : '20-3-2025'   
}]
t1 = Transaction(t1details[1])
print(t1.gettransdetails())
print(t1.deposit(10000))
print(t1.withdraw(5000))
print(t1.withdraw(65000))











        

