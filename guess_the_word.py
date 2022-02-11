from random import randint

with open('words.txt', mode='r', encoding='UTF-8') as words:
    lst = (words.read()).split()


# After read the file with the words and turn it into a list, we're iterating this list to separate
# the words according to the level. Words with less than 5 characters are removed.
easy = []
interm = []
hard = []
for i in lst:
    if len(i) < 5:
        lst.remove(i)
    elif 5 <= len(i) <= 7:
        easy.append(i)
    elif 8 <= len(i) <= 9:
        interm.append(i)
    else:
        hard.append(i)

chances = 7
print(f'\nWelcome to "Guess the word" game - You have {chances} chances to find the secret word\n')
print('[1] - Easy  |  [2] - Intermediate  |  [3] - Hard')
level = input('\nChose the level: ')
while level != '1' and level != '2' and level != '3':
    level = input('Please chose a valid value: ')

# Chosing the word randomly according to the level input
if level == '1':
    secret_word = easy[randint(0, len(easy))]
elif level == '2':
    secret_word = interm[randint(0, len(interm))]
else:
    secret_word = hard[randint(0, len(hard))]

typed = []  # This empty list will receive all the letters that ARE in the secret word
print(f"\nSecret word: {'*' * len(secret_word)}")

while True:
    letter = input('\nChose a letter: ')
    while len(letter) > 1:
        letter = input('Please chose just one letter: ')
    if letter in secret_word:
        print('\nYou got it!')
    else:
        print('\nYou miss it...')
        chances -= 1

    for j in secret_word:
        if j == letter:
            typed.append(j)

    # The temporary word is reset each time and written with the letters in the typed list
    temp_word = ""
    for n in secret_word:
        if n in typed:
            temp_word += n.upper()
        else:
            temp_word += '*'

    # The game ends when the secret word is found or no more chances are left
    if temp_word == secret_word.upper():
        print(f'\nCongratulations! You found the secret word: {temp_word.upper()}')
        break

    elif chances == 0:
        option = input('\nYou lost it... Do you want to know the word? (y/n) ')
        while option.lower() != 'y' and option.lower() != 'n':
            option = input('Please enter a valid value (y/n): ')
        if option.lower() == 'y':
            print(f'\nThe word is {secret_word.upper()}. Thanks for playing!')
            break
        else:
            print('\nThanks for playing!')
            break

    else:
        print(f'\nSecret word: {temp_word}   |   You have {chances} chances remaining!')
