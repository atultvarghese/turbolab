A_UPPERCASE = ord('A')
ALPHABET_SIZE = 25


def get_remainder(number):
   

    while number:
        number, remainder = divmod(number - 1, ALPHABET_SIZE)
        yield remainder


def number_to_alphabet(number1,number2):

    base26_word1 =  ''.join( chr(A_UPPERCASE + part) for part in get_remainder(number1) )[::-1]
    base26_word2 =  ''.join( chr(A_UPPERCASE + part) for part in get_remainder(number2) )[::-1]
    return base26_word1 + base26_word2

def alphabet_to_number(word):
    return sum(
            (ord(letter) - A_UPPERCASE + 1) * ALPHABET_SIZE**i  for i, letter in enumerate(reversed(word.upper()))
    )


word = "petpan"

if len(word)%2:
    print("Please Enter an Even length text")
    exit(0)

first_base10 = alphabet_to_number(word[:int(len(word)/2)])
second_base10 = alphabet_to_number(word[int(len(word)/2):])

total = first_base10 + second_base10
print(total)

print(number_to_alphabet(10145,10039))
