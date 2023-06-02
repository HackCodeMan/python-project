import random
def quess_the_number():
    print("\t\tЯ загадала тебе число от 1 до 1000")
    hidden_number = random.randint(1,1000)
    print("Угадай его за минимальное число попыток ")
    amount_of_tries = 0
    input_value = 0
    while True:
        input_value = int(input("Введи своё предположение: "))
        if input_value > hidden_number:
            print ("Меньше...")
            amount_of_tries += 1
        elif input_value < hidden_number:
            print("Больше...")
            amount_of_tries += 1
        elif input_value == hidden_number:
            print("ДА!!Ты угадал! Моё загаданное число: ",hidden_number,"\nКоличество попыток: ",amount_of_tries)
            break
