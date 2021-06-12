import math

# Method takes a form identical to the Caesarean Cipher method, plus a number shifting case.

def rotationalCipher(str_input, shift):
    str_output      =  ""
    letter_shift    = shift % 26
    for i in str_input:
        if i.isalpha():
            if   i.isupper():
                str_output += chr(((ord(i)-65+letter_shift))%26+65)
            elif i.islower():
                str_output += chr(((ord(i)-97+letter_shift))%26+97)
        elif i.isdigit():
            str_output += str((int(i)+shift)%10)
        else:
            str_output += i
    return str_output

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    input_1 = "All-convoYs-9-be:Alert1."
    rotation_factor_1 = 4
    expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    output_1 = rotationalCipher(input_1, rotation_factor_1)
    check(expected_1, output_1)

    input_2 = "abcdZXYzxy-999.@"
    rotation_factor_2 = 200
    expected_2 = "stuvRPQrpq-999.@"
    output_2 = rotationalCipher(input_2, rotation_factor_2)
    check(expected_2, output_2)

    # Add your own test cases here
