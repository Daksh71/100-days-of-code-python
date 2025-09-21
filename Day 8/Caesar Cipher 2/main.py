alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#

def yes(text1,shift2,direction3):
    if direction3 == "encode":
        encrypt(text1, shift2)
    else:
        decrypt(text1,shift2)

def encrypt(original_text,shift_amount):
    yup=""
    for n in original_text:
        ok=(alphabet.index(n)+shift_amount) % 26
        yup+=alphabet[ok]

    print(yup)


def decrypt(original_text,shift_amount):
    yup1=""
    for n in original_text:
        ok=(alphabet.index(n)-shift_amount )%26
        yup1+=alphabet[ok]

    print(yup1)





yes(text,shift,direction)


# encrypt(original_text=text, shift_amount=shift)



