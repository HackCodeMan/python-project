import pickle
import os
import random
def instruction():
    """Display the instruction"""
    print("""\t\t\t\tС помощью этой программы можно создавать тесты и решать их.
Вы можете, создавая тест, уместить вопросы с вариантами ответов, которые вы или кто то другой будет решать,
открывая в следующий раз ваш тест. Тот кто решает будет набирать количество баллов и после решения он может увидеть
результат в %!!! УДАЧИ ПРИ РЕШЕНИИ ТЕСТА!!!!

       ***            ***
       +              +
       ***            ***
       
       
       ____________________/
       """)
def open_or_create_the_test():
    """User choose open or create the test"""
    print("""\nВы хотите открыть созданный тест или создать новый?
1 - Создать новый тест:)
2 - Открыть существующий тест:|""")
    choice = None
    while choice != "1" and choice != "2":
        choice = input("Ваш выбор: ")
    return choice
def define_choice(message0 = "", message1 = "Ваш выбор: ", variant1 = "Y", variant2 = "N"):
    """Asks the user 'a' or 'b'"""
    choice = None
    while choice != variant1 and choice != variant2:
        print(message0)
        print(message1, "(", variant1, "/", variant2, "): ", sep="", end ="")
        choice = input().upper()
    return choice
def input_questions_wrong_correct(question_number):
    """User enters questions and answer options"""
    print("\nВведите ",question_number+1,"-вопрос: ",sep = "", end="")
    question = input()
    print("Теперь введите правильный ответ: ", end="")
    correct = input()
    wrong_array = []
    print("Введите варианты неправильных ответов, когда закончите нажмите \"Enter\" без ввода данных:)")
    end = False
    while end != True:
        input_end = False
        while input_end != True:
            wrong = input()
            if wrong != "":
                wrong_array.append(wrong)
            else:
                input_end = True
        if len(wrong_array) != 0:
            end = True
        else:
            print("Нет не правильных? Дружок это не квест, а фигня. Переделывай")
            continue
    print("Ваш",question_number+1,"-вопрос:", question)
    print("Правильный ответ:", correct)
    print("Варианты неправильных", wrong_array)
    return question, correct, wrong_array
def save_exercise (correct, wrong_array, question_answer, question, test_name, questions):
    """Saving the question with answers"""
    if not os.path.exists("tests"):
        os.mkdir("tests")
    location = "tests\\" + test_name + ".dat"
    test = open(location,"wb")
    pickle.dump(question_answer, test)
    pickle.dump(questions, test)
    test.close()
def create_the_test():
    """Create the test"""
    test_created = False
    while not test_created:
        print("\nВы сейчас создаёте новый тест.\nОткрытие теста можете совершить только в программе")
        print("Введите как будет называться ваш тест. Он сохранится в папку tests ")
        test_name = input("\nИмя теста: ")
        questions = []
        question_answer = {}
        input_questions_test = False
        question_number = 0  #the value of the total number of questions in the test
        variants_of_answers = 0
        while input_questions_test != True:
            question, correct, wrong_array = input_questions_wrong_correct(question_number)
            сonfirmation = define_choice(message1 = "Уверены? ")
            if сonfirmation.upper() == "Y":
                questions.append(question)
                question_answer[question] = [correct, wrong_array]
                question_number += 1
                variants_of_answers += 1
            elif сonfirmation.upper() == "N":
                choice = define_choice(message0 = """Ok.Попробуете еще раз или не хотите создать задание
        1 - Попробывать ещё раз
        2 - Не хочу создавать Задание""",variant1 = "1",variant2 = "2")
                if choice == "2":
                    input_questions_test = True
            choice = define_choice(message0 = "Хотите продолжить ввод вопросов?",variant1 = "Y",variant2 = "N")
            if choice == "Y":
                print("\nЗадание записано\n")
                continue
            else:
                save_exercise(correct, wrong_array, question_answer, question, test_name,
                              questions)
                input_questions_test = True
                test_created = True
                print("\nТест создан\n")
def display_exercise(correct_answer,wrong_answers_array,question):
    """Display the question and variants of answers"""
    variants_of_answers = wrong_answers_array
    variants_of_answers.append(correct_answer)
    print(question)
    used_variants = []
    i = 0
    while i < len(variants_of_answers):
        variant_of_answer = random.choice(variants_of_answers)
        if variant_of_answer not in used_variants:
            print(variant_of_answer)
            used_variants.append(variant_of_answer)
            i += 1
        else:
            continue
def scoring(questions_with_correct_answers,questions_with_wrong_answers, questions):
    max_score = len(questions)
    user_score =  len(questions_with_correct_answers)
    user_score_in_percent = str(abs((user_score / max_score)*100)) + "%"
    print("Вы решили тест на", user_score_in_percent)
    print("Правильно ответили на", user_score,"вопросов")
    print("Неправильно ответили на", len(questions_with_wrong_answers), "вопросов")
def open_the_test():
    """Open the test"""
    choice = define_choice(message0 = """1 - Открыть тест
2 - Посмотреть список созданных тестов""", variant1="1",variant2="2")
    if choice == "1":
        print("Введите имя теста. Он должен находиться в папке tests, а иначе программа не увидит его:\ ")
        test_name = input("Имя теста: ")
        if test_name[-4:] != ".dat":
            location = "tests\\" + test_name + ".dat"
        else:
            location = "tests\\" + test_name
        if os.path.exists(location):
            test = open(location,"rb")
            question_answer = pickle.load(test)
            questions = pickle.load(test)
            amount_solved_questions = []
            questions_with_correct_answers = []
            questions_with_wrong_answers = []
            while len(amount_solved_questions) != len(questions):
                question = random.choice(questions)
                if question not in amount_solved_questions:
                    correct_answer = question_answer[question][0]
                    wrong_answers_array = question_answer[question][1]
                    display_exercise(correct_answer,wrong_answers_array,question)
                    user_answer = input("Ваш выбор: ")
                    if user_answer == correct_answer:
                        questions_with_correct_answers.append(question)
                    else:
                        questions_with_wrong_answers.append(question)
                    amount_solved_questions.append(question)
                else:
                    continue
            scoring(questions_with_correct_answers,questions_with_wrong_answers, questions)
        else:
            print("Такого теста нет. Попробуйте снова")
    else:
        print("Список тестов:")
        list_tests = os.listdir("tests")
        print("\n".join(list_tests))
def QUIZ():
    """Main program"""
    instruction()
    choice = None
    while choice != "":
        print("""Вы хотите открыть созданный тест или создать новый?
            1 - Создать новый тест:)
            2 - Открыть существующий тест:|""")
        choice = input("Ваш выбор: ")
        if choice == "1":
            create_the_test()
        elif choice == "2":
            open_the_test()
        elif choice == "":
            break
QUIZ()
input("\n\n Нажмите 'Enter', чтобы выйти")