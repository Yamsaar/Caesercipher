from art import Art_Logo as Logo


List_Alphabet = [
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(f"{Logo} \n")

choice = input("Hello, please chose if you want to 'encode' to encrypt or 'decode' to decrypt:\n ")


txt_massage = list(input("please enter a massage:\n ").lower())
# txt_massage get only lower case latter from input.

shift = int(input("please enter number of shifts:\n "))
# help to encode or decode a massage by shifting the latter from the massage and decode or incode.

game_over = False

'''the operation run till the flag changing to True
according to user choice to decrypt or encrypt an input
the final text will be decoded or encoded output. '''

while not game_over:
    if choice == 'encode':
        for ch in range(len(txt_massage)):
            if txt_massage[ch] == ' ':
                txt_massage[ch] = ' '
            else:
                location = List_Alphabet.index(txt_massage[ch])
                new_location = location + shift
                txt_massage[ch] = List_Alphabet[new_location]
        print(' '.join(txt_massage))
        game_over = True
    elif choice == 'decode':
       for ch in range(len(txt_massage)):
           if txt_massage[ch] == ' ':
               txt_massage[ch] = ' '
           else:
               location = List_Alphabet.index(txt_massage[ch])
               new_location = location - shift
               txt_massage[ch] = List_Alphabet[new_location]
       print(' '.join(txt_massage))
       game_over = True
    else:
        user = input("Invalid tayping please try again, enter Y for yes or N for no: \n").lower()
        if user == 'Y':
            choice = input("Hello, please chose if you want to 'encode' to encrypt or 'decode' to decrypt:\n ")
            txt_massage = list(input("please enter a massage:\n ").lower())
            shift = int(input("please enter number of shifts:\n "))
        else:
            game_over = True
