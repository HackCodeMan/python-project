import random
GUESS_WORDS = ("машина","посудомойка","абрикос","геометрия","самолёт","вселенная","галактика","вертолёт",
               "ракета","ластик", "книга", "садовод", "деньги","транспортир","информатика","микрофон","шаман",
               "микроволновка","розетка","помещение","лампочка","игрушка","мальчик","любовь","чувства","гениальность")
hidden_word = GUESS_WORDS[random.randrange(len(GUESS_WORDS))]
anagram = ''
while int(len(anagram)) != int(len(hidden_word)):
    new_ordinal_number = random.randrange(len(hidden_word))
    if hidden_word[new_ordinal_number] not in anagram:
        anagram += hidden_word[new_ordinal_number]
print("\t\t\t\tWelcome in the Game 'Anagram'!!\nNeed to Rearrange the Letters in the Word, so that you get a MEANINGFUL\
 WORD!!")
print("For exit click 'Enter', without enter your guess:( ")
answer = None
guessed = False
tries = 0
while not guessed:
    print("Anagram: ", anagram)
    answer = input("Enter your guess: ")
    if answer:
        if answer.lower() == hidden_word:
            guessed = True
        else:
            print("My hidden word didn't match your answer\n")
            tries += 1
print("Well done!! You are guessed!!!!:))) My hidden word is", hidden_word)
print("Amount of tries: ",tries)
input("\n\nClick 'Enter', to exit:(")




