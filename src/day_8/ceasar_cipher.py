from ..day_8.ceaser_cipher_constants import ceaser, cipher, letters


def ceaser_cipher():
    print(ceaser)
    print(cipher)

    continue_running = True
    while continue_running:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        message = input("Type your message:\n").lower()
        shift_number = int(input("Type the shift number:\n"))

        match direction:
            case "encode":
                result = encode(message, shift_number)
                print(f"Here's the encoded result: {result}")
            case "decode":
                result = decode(message, shift_number)
                print(f"Here's the decoded result: {result}")
            case _:
                continue

        continue_running = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower() == 'yes'


def encode(message, shift_number):
    result = ""
    for ch in message:
        index = letters.index(ch) + shift_number % len(letters)
        result += letters[index]

    return result


def decode(message, shift_number):
    result = ""
    for ch in message:
        index = letters.index(ch) - shift_number % len(letters)
        result += letters[index]

    return result
