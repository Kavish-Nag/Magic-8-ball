import random

ans = True

while ans:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")
    
    answers = random.randint(1,15)
    
    if question == "":
        exit()
    
    elif answers == 1:
        print("It is certain")
    
    elif answers == 2:
        print ("Without a doubt")
    
    elif answers == 3:
        print ("Yes – definitely")
    
    elif answers == 4:
        print ("Ask again later")
    
    elif answers == 5:
        print ("Concentrate and ask again")
    
    elif answers == 6:
        print ("You may rely on it")
    
    elif answers == 7:
        print ("My reply is no")
    
    elif answers == 8:
        print ("Most likely")

    elif answers == 9:
        print("My reply is Yes.")

    elif answers == 10:
        print("Yes Signs point to yes")

    elif answers == 11:
        print("Of course.")

    elif answers == 12:
        print("Better not tell you now")

    elif answers == 13:
        print("Cannot predict now")

    elif answers == 14:
        print("Very doubtful")

    
