import random
print("\t\tWelcome in the game 'Guess The Number':)")
hidden_number = random.randint(1,1000)
print("\nI guessed the number in range 1 to 1000")
print("Try to guess the number for the minimum amount of tries! GOOD LUCK;) ")
amount_of_tries = 0
input_value = 0
while True:
    input_value = int(input("Enter your guess: "))
    if input_value > hidden_number:
        print ("Less...")
        amount_of_tries += 1
    elif input_value < hidden_number:
        print("More...")
        amount_of_tries += 1
    elif input_value == hidden_number:
        print("Yes!!You guessed! My hidden number is",hidden_number,"\nAmount of tries is",amount_of_tries)
        break
input("Click 'Enter', to exit:)")