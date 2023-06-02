import time
print("This Game Do Not Like Vowels.")
text = input("Enter the text: ")
new_text = ""
vowels = "АЕЁИОУЭЮЯыЫаеёиоуэюяaiouyeIOUYE"
for letter in text:
    if letter not in vowels:
        new_text += letter
        time.sleep(0.2)
        print("Created a new string:",new_text)
print("This is your text without vowels:", new_text)
input("\n\n Click 'Enter', to exit.")
