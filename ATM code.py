import time

def balance(saving):

    print(f"Your Balance is {saving}")

def deposite(amount):
    if amount <= 0:
        print("Please Enter a Valid Amount\n")
        return 0
    else:
        time.sleep(1)
        print("Your Amount has been Successfully Deposited\n")
        return amount

def withdraw(amount,saving):
        if amount > saving :
            print("You have insufficient Bank Balance\n")

        elif amount<=0:
            print("You have entered a invalid amount\n")

        else:
            time.sleep(1)
            print("THE amount has been withdrawn successfully \n")
            return amount



def main():

    saving=0
    trans="Y"

    print("WELCOME\n")
    while trans=="Y":

        print("1.Balance \n2.Deposite \n3.Withdraw ")
        option = int(input())

        match option:
                case 1:
                    balance(saving)
                    trans=input("Do you want to continue your transaction (Y/N) :").upper()
                case 2:
                    amount = int(input("Enter the amount you want to deposite : \n"))
                    amount = deposite(amount)
                    saving+=amount
                    trans = input("Do you want to continue your transaction (Y/N) :").upper()
                case 3:
                    amount=int(input("Enter the amount you want to withdraw : \n"))
                    amount = withdraw(amount,saving)
                    if amount:
                        saving-=amount
                    trans = input("Do you want to continue your transaction (Y/N) :").upper()
                case _:
                    print("Invalid input")
                    trans = input("Do you want to continue your transaction (Y/N) :").upper()
    print("Have a Nice Day")



if __name__ =='__main__':
    main()