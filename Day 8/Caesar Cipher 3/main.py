# import art
# print(art.logo)
#


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
cont=input("do the user want to continue or not pls select two type yes or no .")


def encrypt(original_text,shift_amount):
    yup=""
    for n in original_text:
        if n in alphabet:
            ok=(alphabet.index(n)+shift_amount) % 26
            yup+=alphabet[ok]
        else:
            yup+= n
    print(f"Encrypted code is {yup}")


def decrypt(original_text,shift_amount):
    yup1=""
    for n in original_text:
        if n in alphabet:
            ok=(alphabet.index(n)-shift_amount) % 26
            yup1+=alphabet[ok]
        else:
            yup1+= n

    print(f"decrypted code is {yup1}")


def yes(text1,shift2,direction3,cont1):
    while cont1 == "yes":
        if direction3 == "encode":
            encrypt(text1, shift2)
        elif direction3=="decode":
            decrypt(text1,shift2)
        else:
            print("Invalid INPUT")
            break



yes(text,shift,direction,cont)