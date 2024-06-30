import codecs
import string
from collections import Counter

def score_string(text):
    # Define the 7 most common characters in English
    common_characters = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D']

    # Initialize score
    score = 0

    # Count occurrences of each common character
    char_count = {char: text.upper().count(char) for char in common_characters}

    # Sum up the scores based on occurrence
    score = sum(char_count[char] for char in common_characters)

    return score

def score_string_by_bigrams(text):
    # Define common letter pairs (bigrams) in English
    common_bigrams = ['TH', 'HE', 'AN', 'RE', 'ER', 'IN', 'ON', 'AT', 'ND', 'ST', 'ES', 'EN', 'OF', 'TE', 'ED', 'OR', 'TI', 'HI', 'AS', 'TO']

    # Convert text to uppercase to standardize
    text = text.upper()

    # Initialize score
    score = 0

    # Count occurrences of each bigram
    bigram_counts = Counter(text[i:i+2] for i in range(len(text) - 1))

    # Sum up the scores based on occurrence of common bigrams
    score = sum(bigram_counts[bigram] for bigram in common_bigrams)

    return score

# Decode the hex string
hex_encoded = "220e2133054727002601333e18090102720f231637281e7b141a0a1520200432157800043e233a08"
decoded = codecs.decode(hex_encoded, 'hex').decode()

# Break the string into columns
matrix = [[]]
matrix[0] = [decoded[i] for i in range(len(decoded)) if i % 5 == 0]
matrix.append([])
for i in range(len(decoded)):
    if ((1 + 5 * i) < len(decoded)):
        matrix[1].append(decoded[1+5*i])
matrix.append([])
for i in range(len(decoded)):
    if ((2 + 5 * i) < len(decoded)):
        matrix[2].append(decoded[2+5*i])
matrix.append([])
for i in range(len(decoded)):
    if ((3 + 5 * i) < len(decoded)):
        matrix[3].append(decoded[3+5*i])
matrix.append([])
for i in range(len(decoded)):
    if ((4 + 5 * i) < len(decoded)):
        matrix[4].append(decoded[4+5*i])


# Get the possible character for each column
# Make a assumption that the flag contains only number, letter and {}
guess_key = []
for column in range(0,5):
    guess_key.append([])
    for guess_char in list(string.ascii_letters + string.digits):
        printable = True
        collection = []
        for index in range(len(matrix[column])):
            result = chr(ord(guess_char) ^ ord(matrix[column][index]))
            # if (result not in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"):
            if (result not in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}"):
                printable = False
                break
            else:
                collection.append(result)
        if (printable):
            guess_key[column].append(guess_char)

# Brute-forcing with scoring function
for first in guess_key[0]:
    for second in guess_key[1]:
        for third in guess_key[2]:
            for fourth in guess_key[3]:
                for fifth in guess_key[4]:
                    key = first + second + third + fourth + fifth
                    assumption = ""

                    for i in range(0,len(decoded)):
                        assumption += chr(ord(decoded[i]) ^ ord(key[i%len(key)]))
                    if (score_string(assumption) >= 20 and score_string_by_bigrams(assumption) >= 4):
                        print(f"Guess: {assumption} with key {key}")