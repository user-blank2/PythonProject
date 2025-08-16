
import random

def Ask_user(dict,used):

    if not used:
        print("DRAW WATCH")
        return

    user_input=input("Enter THE POSITION :")

    if  (not user_input.isdigit()) or dict[user_input]=="X" or dict[user_input]=="O":
        print("Please enter a valid position .... \n")
        return "Invalid"

    used.remove(user_input)
    dict[user_input]="X"



def Ask_bot(dict,used):

    if not used:
        print("Draw Match ....")
        return

    bot=random.choice(used)
    used.remove(bot)
    dict[bot]="O"

def choose_win(dict,N):
        win=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]


        for ch in win:
            a,b,c=ch
            a=str(a)
            b=str(b)
            c=str(c)
            if dict[a]==dict[b]==dict[c]  and dict[a] != " ":

                return dict[a]

        return True

def main():
    dict={"1": " ","2": " ","3": " ","4": " ","5": " ","6": " ","7": " ","8": " ","9": " ",}
    used=["1","2","3","4","5","6","7","8","9"]
    is_run=True
    run=""
    while is_run:
        N = f" {dict['1']} | {dict['2']} | {dict['3']} \n---|---|---\n {dict['4']} | {dict['5']} | {dict['6']} \n---|---|---\n {dict['7']} | {dict['8']} | {dict['9']} "

        if run=="X" or run=="O":
            print(N)
            print(f"{run} wins")
            break
        print(N)

        res = Ask_user(dict,used)

        if res != "Invalid":
            Ask_bot(dict,used)

        run = choose_win(dict, N)

if __name__=='__main__':
    main()