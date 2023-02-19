alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 
             'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = str(input("Type your message:\n").lower())
    shift = int(input("Type the shift number:\n"))
    shift=shift%26



    if direction=="encode":
        def encrypt(text, shift):

            cipher_word=""

            for i in text:
                if i in alphabet:

                    position=alphabet.index(i) #word 1st alphabet index position in the 26 alphas
                    new_index=position+shift #shift by how many is added new index
                    cipher=alphabet[new_index] #new index letter from alpha is putted in cipher
                    cipher_word=cipher_word+cipher #new empty string forms the word by adding the chipher word each iterations

                else:
                    cipher_word=cipher_word+i


            print("encoded text", cipher_word)
    
        encrypt(text, shift)

    elif direction=="decode":
        def decrypt(text, shift):

            decipher_word=""

            for i in text:
                if i in alphabet:
                    position=alphabet.index(i)
                    new_index=position-shift
                    decipher=alphabet[new_index]
                    decipher_word=decipher_word+decipher

                else:
                    decipher_word=decipher_word+i  

            print("unencoded text", decipher_word)

        decrypt(text, shift)

    else:
        print("nalle")

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if restart=="no":
        should_continue=False
        print("Goodbye")


# #-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#       shift_amount *= -1
#   for letter in start_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     end_text += alphabet[new_position]
#   print(f"Here's the {direction}d result: {end_text}")


# #-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

