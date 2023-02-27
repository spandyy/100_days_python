# morse_code = {
#     'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 
#     'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
#     'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 
#     's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 
#     'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---',
#     '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
#     '8': '---..', '9': '----.'
# }

# def text_to_morse(text):
#     morse = ''
#     for char in text.lower():
#         if char in morse_code:
#             morse += morse_code[char] + ' '
#         elif char == ' ':
#             morse += '  '
#     return morse

# # Example usage:
# text = 'Hello, world!'
# morse = text_to_morse(text)
# print(morse)


TEXT_TO_MORSE = {
    'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.',
    'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.','Q':'--.-', 'R':'.-.', 'S':'...','T':'-','U':'..-',
    'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----',
    '2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...',
    '8':'---..','9':'----.','0':'-----', ' ': '/', '.':'.-.-.-', ',':'--..--',
    '?':'..--..',"'":'.----.','!':'-.-.--', '/':'-..-.','(':'-.--.',')':'-.--.-',
    ':':'---...',';':'-.-.-.', '"':'.-..-.'
}
# bb={}
# print(TEXT_TO_MORSE.items())
MORSE_TO_TEXT = {value:key for key,value in TEXT_TO_MORSE.items()}
# for key,value in TEXT_TO_MORSE.items():
#     bb[value]=key

# print(bb)

def to_morse(msg):
    morse_message = ''
    msg = msg.upper()
    for letter in msg:
        morse_message+=TEXT_TO_MORSE[letter]
        morse_message+=' '
    return morse_message


def to_text(msg):
    text_message = ''
    msg =msg.split()
    for letter in msg:
        text_message+=MORSE_TO_TEXT[letter]
    text_message=text_message.capitalize()
    return text_message


def continue_use():
    using=True
    option = input('Do you want to continue using the translator? Type Y or N\n')
    option = option.upper()
    if option == 'N':
        using = False
    return using


in_Use= True
print('Welcome to the Python Morse Code translator')
while in_Use:
    menu = input('Select an option to translate (Type the number)\n'
                 '1)Convert text to morse code\n'
                 '2)Covert morse code to text\n')
    if menu == '1':
        message = input('Type the message you want to translate to Morse Code\n')
        translated_message = to_morse(message)
        print(f'This is your message in morse code: {translated_message}')
    elif menu == '2':
        message = input('Type the message you want to translate to text\n')
        text_message = to_text(message)
        print(f'This is what the morse code says: {text_message}')
    in_Use = continue_use()
print('Thank you for using the Morse Code Translator')