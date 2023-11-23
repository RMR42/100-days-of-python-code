alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# done using a single funtion

def ceasar(input_text,shift_amount,caesar_command):
    final_text =''
    alphabet_length = len(alphabet)

    for letter in input_text:
            if letter in alphabet:
                if caesar_command == 'decode':
                    new_letter_index = alphabet.index(letter) - shift_amount
                    final_text += alphabet[new_letter_index]
                if caesar_command == 'encode':
                    new_letter_index = alphabet.index(letter) + shift_amount - alphabet_length
                    final_text += alphabet[new_letter_index]
            else:
                final_text += ' '

    print(final_text)

ceasar(text,shift,direction)
        

## Long Form

# def encrypt(text,shift):
#     cipher_text = ''
#     for letter in text:
#         if letter in alphabet:
#             new_letter_index = alphabet.index(letter) + shift - len(alphabet)
#             cipher_text += alphabet[new_letter_index]
#         else:
#             cipher_text += ' '

#     print(cipher_text)
        
# def dycrypt(text,shift):
#     cipher_text = ''
#     for letter in text:
#         if letter in alphabet:
#             new_letter_index = alphabet.index(letter) - shift
#             cipher_text += alphabet[new_letter_index]
#         else:
#             cipher_text += ' '

#     print(cipher_text)

# if direction == 'encode':
#     encrypt(text,shift)
# elif direction == 'decode':
#     dycrypt(text,shift)
# else:
#     print('Sorry, you have to choose between "encode" or "decode"')
