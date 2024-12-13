# part #2

# cleaned up code in decrypt function - used variables from course
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.

# def decrypt(original_text, shift_amount):
#     uncipher_text = ""
#     for letter in original_text:
#         unshifted_position = alphabet.index(letter) - shift_amount
#         unshifted_position %= len(alphabet)
#         uncipher_text += alphabet[unshifted_position]
#     print(f"Here is the decoded result: {uncipher_text}")
#
# decrypt(text, shift)

# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    # multiplying by a negative is the same as subtracting
    # in the below code, if "decode" is triggered, it will flip the shifted_position code to subtract
    if encode_or_decode == "decode":
         shift_amount *= -1
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

caesar(text, shift, direction)

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")
#
#
# encrypt(text, shift)



