from word_collection import name

def hang_man(wng):

   print("\n".join(hans_man[wng]))

def guesses(plat):
    global wng_guess

    print(*plat)

    guess=input("Guess the animal letter : ").lower()
    if len(guess)!=1 or not guess.isalpha():
        print("Enter a valid guess...")
        return plat

    if guess in name:

        if guess in crt_guess:
            print("This guess already exist...")
            return plat


        crt_guess.append(guess)

        for i in range(len(name)):
            if guess == name[i]:
                 plat[i]=guess
        return plat

    else:

        print("wrong guess")
        wng_guess+=1
        return plat

hans_man={
    0:("      ",
       "      ",
       "      "),
    1:("  O   ",
       "      ",
       "      "),
    2:("  O   ",
       "   |  ",
       "      "),
    3:("   O  ",
       "  /|  ",
       "      "),
    4:("   O  ",
       "  /|\\",
       "      "),
    5:("   O  ",
       "  /|\\",
       "  /   "),
    6:("   O  ",
       "  /|\\",
       "  / \\"),
}


print("Guess the animal name....")




wng_guess=0
crt_guess=[]


def main():
     plat = "_" * len(name)
     plat =list(plat)
     is_run=True

     while is_run:
         hang_man(wng_guess)

         if wng_guess==len(hans_man)-1:
            print("You lost Dumb ...")
            print(f"ANSWER is {name}")
            break


         plat = guesses(plat)


         if "_" not in plat:
             print(*plat)
             print("YOU WON...congralations")
             break





if __name__=="__main__":
    main()