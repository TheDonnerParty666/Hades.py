questionOneCorrect = 0
print("Welcome to Hadestown.  Didn't you learn the first time?") 
print("First Level.")
while questionOneCorrect == 0:
    print("How many pomegrantes did Persephone eat that doomed her to shared time in Hell?")
    questionOneAnswer = raw_input()
    questionOneAnswer = str(questionOneAnswer)
    if str.lower(questionOneAnswer) == "six":
        print("What? Where am I? You need to stop! Don't go further.")
        questionOneCorrect = 1
    elif questionOneAnswer == "6":
        print("What? Where am I? You need to stop! Don't go further.")
        questionOneCorrect = 1
    else:
        print("FAILURE!")
questionTwoCorrect = 0
print("Second Level.")
while questionTwoCorrect == 0:
    print("How many heads does Ceberus have?")
    questionTwoAnswer = raw_input()
    questionTwoAnswer = str(questionTwoAnswer)
    if str.lower(questionTwoAnswer) == "three":
        print("@&#$&#@*><':")
        questionTwoCorrect = 1
    elif questionTwoAnswer == "3":
        print("@&#$&#@*><':")
        questionTwoCorrect = 1
    else:
        print("WRONG!")
questionThreeCorrect = 0
print("Next level.")
while questionThreeCorrect == 0:
    print("WHO IS PERSEPHONE?")
    questionThreeAnswer = raw_input()
    questionThreeAnswer = str(questionThreeAnswer)
    if str.lower(questionThreeAnswer) == "queen of the underworld":
        print("Pay no attention to him. Continue!")
        questionThreeCorrect = 1
    elif str.lower(questionThreeAnswer) == "hades wife":
        print("Pay no attention to him. Continue!")
        questionThreeCorrect = 1
    elif questionOneAnswer == "greek goddess":
        print("Pay no attention to him. Continue!")
    elif questionOneAnswer == "goddess of the underworld":
        print("Pay no attention to him. Continue!")
    elif questionOneAnswer == "demeter's daughter":
        print("Pay no attention to him. Continue!")
    else:
        print("Please!!! just leave if you kno---- Try again and continue.")
print("Fourth question.")
questionFourCorrect = 0
while questionFourCorrect == 0:
    print("What realm does Hades reside over?")
    questionFourAnswer = raw_input()
    questionFourAnswer = str(questionFourAnswer)
    if questionFourAnswer == "hell":
        print("He is no longer a problem.")
        questionFourCorrect = 1
        questionFourAnswer = raw_input()
    questionFourAnswer = str(questionFourAnswer)
    if questionFourAnswer == "He is no longer a problem.":
        print("Correct!")
        questionFourCorrect = 1
    else:
        print("WRONG!!!")
print("WHY DO YOU KEEP PLAYING? STOP N--- Please continue")
questionFiveCorrect = 0
while questionFiveCorrect == 0:
    print("From what mythos do Hades and Persephone reside?")
    questionFiveAnswer = raw_input()
    if str.lower(questionFiveAnswer) == "greek":
        print("STOP!! NO! THEY WILL KILL Y--- How does that keep happening? He is more persistent than we thought.")
        questionFiveCorrect = 1
    else:
        print("STOP!! NO! THEY WILL KILL Y--- How does that keep happening? Try again.")

for count in range(100):
          print("")
print("Well done... https://sites.google.com/share.brevardschools.org/guesswho/home")
