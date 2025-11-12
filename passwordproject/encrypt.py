import string
# from random import shuffle

chars = " " + string.punctuation + string.digits + string.ascii_letters
"""keymaking
#chars = list(chars)
key = shuffle(chars)
"""
key = ['9', '<', 'y', ']', 'x', 't', '$', '?', '}', 'A', '3', 'G', 'e', '*', 'E', '>', '5', 'l', ',', ';', 'M', 'P', 'W', 'H', '=', 'Z', '&', '/', 'q', 'z', '6', '"', 's', '!', '^', '4', 'k', 'r', 'R', '@', 'K', '2', 'L', '.', 'g', 'c', 'D', 'T', 'I', "'", '%', '_', '-', 'v', '7', '~', '`', '0', 'm', ':', 'u', 'N', 'a', 'S', 'h', '[', '\\', '#', 'J', ' ', 'F', 'd', '1', 'U', 'X', 'O', 'b', '(', 'o', 'B', 'w', 'n', 'C', 'i', '8', ')', 'V', 'p', '+', '|', 'f', 'Q', '{', 'j', 'Y']



def encrypt(txt):
    encryptedtxt = ""

    for letter in txt:
        index = chars.index(letter)
        encryptedtxt += key[index]

    return encryptedtxt

def decrypt(txt):
    plaintxt = ""

    for letter in txt:
        index = key.index(letter)
        plaintxt += chars[index]

    return plaintxt


def main():
    pass


def check_validity(password):
    # stored values for the checks if they are true or not if its set true that means the condition is met

    val1 = len(password) >= 6 #if length is long enough for safety (returns false if this isnt true)
    val2 = False #if there is atleast one uppercase
    val3 = False # if there is a digit
    val4 = False # if there is a specal character
    val5 = False  # atleast one lower
    val6 = False # if there is spaces in it

    # the checking
    for char in password:
        if char.isupper():
            val2 = True
        if char.isdigit():
            val3 = True
        if not char.isalnum():
            val4 = True
        if char.islower():
            val5 = True
        if char.isspace():
            val6 = True

    missing = []
    if not val1:
        missing.append("at least 6 characters\n")
    if not val2:
        missing.append("an uppercase letter\n")
    if not val5:
        missing.append("a lowercase letter\n")
    if not val3:
        missing.append("a digit\n")
    if not val4:
        missing.append("a special character\n")
    if val6:
        missing.append("no spaces in password\n")

    if not missing:
        return  True
    else:
        return "Password is invalid ❌. You need to add: "+ "".join(missing)




if __name__ == '__main__':
    main()

