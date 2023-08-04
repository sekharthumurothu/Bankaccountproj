
from bank_account2 import *
b = ['1.Normal account', '2.Interest Rewards Account', '3. Savings Account']
f = ["1.Deposit","2.withdraw", "3.Transfer"]
print("\nPlease choose from the following options:\n")
a = ['1.Create a Bank Account and Deposit', "2.getBalance", "3.Deposit","4.withdraw", "5.Transfer"]
for word in a:
    print(word)
c = int(input(f'\nEnter your choice: '))
if c ==1:
    d = print("What type of account you would like to open:")
    for word in b:
        print (word)
    e = int(input("Enter your choice: "))
    if e ==1:
        account = BankAccount()
        account.getBalance()
        print('Do you want to perform any of the following:')
        for word in f:
            print(word)
        g = int(input("Enter your choice: "))
        if g ==1:
            account.deposit()
        elif g ==2:
            account.withdraw()
        else:
            account.transfer()
    elif e == 2:
        intacct = InterestRewarsAcct()
        intacct.getBalance()
    else:
        savacct = SavingsAcct()
        savacct.getBalance()
if c == 3:
    account.deposit()






