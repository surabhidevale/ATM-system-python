balance=0

def check_balance():
    print("Total balance in your account is =",balance)
def deposit_cash(amt):
    global balance
    balance=balance+amt #0+2000 balance=200
    print(amt,"Rs.Deposited")
def withdraw_cash(amt):
    global balance
    if amt <=balance:
        balance=balance-amt
        print(amt,"Rs.Withdrawn")
    else:
        print("Insufficient Balance")

while True:
    ch=int(input("\nENTER CHOICE :\n1.CHECK BALANCE \n2.DEPOSIT AMOUNT\n3.WITHDRAW AMOUNT \n4.EXIT : "))
    print()
    if ch==1:
        check_balance()
    elif ch==2:
        d_amt=int(input("Enter amount to deposit ="))
        deposit_cash(d_amt)
    elif ch==3:
        w_amt=int(input("Enter amount to withdraw ="))
        withdraw_cash(w_amt)
    elif ch==4:
        print("Transaction completed")
        break
    else:
        print("INVALID CHOICE")


