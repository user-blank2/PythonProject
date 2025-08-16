import random
def rand(bet):
    choices=['🍓','🍉','🍎','⭐','💖']
    res=[random.choice(choices) for _ in range(3)]
    print(" ".join(res))
    return res



def tot(res,bet):
    if res[0]==res[1]==res[2]:
        if res[0]=='🍓':
            win=bet*2
        elif res[0]=='🍉':
            win=bet*4
        elif res[0] == '🍎':
            win=bet*6
        elif res[0] == '⭐':
            win=bet*8
        else:
            win=bet*10
    else:
        win=0
    return win



def main():

    print("Lets Gamble ....")
    bet_tot = 100
    print(f"Your have {bet_tot}")
    while bet_tot > 0:


        bet=input("Enter your bet amount :")

        if  not bet.isdigit():
            print("Please enter a proper bet amount :")
            continue



        if int(bet) > bet_tot:
            print("You dont have sufficient balance... ")
            continue

        bet = int(bet)
        bet_tot-=bet


        res = rand(bet)
        win_amt = tot(res,bet)
        bet_tot+=win_amt

        if win_amt == 0:
            print("You lost your bet ! ")
            print(f"Your current balance is {bet_tot}\n")
        else:
            print("Wow... you won")

        n=input("Do you still want to gamble ? Press 'N' to exit or press any key to contuinue your gambling\n").upper()
        if n == "N":
            exit()
        else:
            if bet_tot<=0:
                print("lol...you have no money  \n Go to work")
                exit()



if __name__ == '__main__':
    main()