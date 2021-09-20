"""
1p - algorithm for the method of successive divisions

1p - algorithm for the substitution method

1p – algorithm for conversion using 10 as an intermediate base

2p - rapid conversions (executable form) between two bases p,q={2, 4, 8, 16}.

1p addition of two numbers in a base

1p subtraction of two numbers in a base

1p multiplication of a number by a digit in a base

1p division of a number by a digit in a base

1p code quality (indentation, use of comments, suggestive variables names)
"""


def print_menu():
    print("---------Algorithm made by Hincu Alice Ramona---------")
    print("What do you want to do?")
    print("\t1. Covert two numbers")
    print("\t2. Addition of two numbers in a base")
    print("\t3. Subtraction of two numbers in a base")
    print("\t4. Multiplication of a number by a digit in a base")
    print("\t5. Division of a number by a digit in a base")


def input_and_check_base():
    """ Input and verification of a base, that it is a positive integer
        between 2-10 and 16.
    :return: the base as an integer.
    """
    while True:
        base = input("Base: ")
        # if the base has only digits and the number is in the given interval
        if base.isdigit() and (1 < int(base) < 11 or int(base) == 16):
            return int(base)
        else:
            raise ValueError("The base should be between 2-10 and 16")


def input_and_check_number(base):
    """ Input and verification of starting number, that it is a positive integer
        using only characters from its base. Returns starting_num as a string.
    """
    # Assigns string which only contains characters from the given base
    base_members = ".0123456789ABCDEF"[0:base+1]

    while True:
        number = input("Number: ")
        if all(digit in base_members for digit in number):
            # if every digit in the number is from the base
            return number
        else:
            raise ValueError("Please only use characters in your base (Capital letters for " +
                             "bases larger than than 10)")


def input_bases_and_numbers():
    """
        Menu for the 2 bases.
    :return: the bases as integers
    """
    print("\n---Convert number(insert the number and its source base, followed by the destination base---")
    base_1 = input_and_check_base()
    number_1 = input_and_check_number(base_1)
    print("---To base---")
    base_2 = input_and_check_base()
    return base_1, number_1, base_2


def input_and_print_menu_addition():
    """
    Print menu for addition
    :return:
    """
    print("---For addition of 2 numbers----")
    base = input_and_check_base()
    nr_1 = input_and_check_number(base)
    nr_2 = input_and_check_number(base)
    return base, nr_1, nr_2


def input_and_print_menu_subtraction():
    """
    Print menu for subtraction
    :return:
    """
    print("---For subtraction of 2 numbers(Subtract from the biggest number)----")
    base = input_and_check_base()
    nr_1 = input_and_check_number(base)
    nr_2 = input_and_check_number(base)
    return base, nr_1, nr_2


def input_and_print_menu_multiplication():
    """
    Print menu for multiplication
    :return:
    """
    print("---For multiplication of 2 numbers(one must be a digit)----")
    base = input_and_check_base()
    nr_1 = input_and_check_number(base)
    nr_2 = input_and_check_number(base)
    return base, nr_1, nr_2


def input_and_print_menu_division():
    """
    Print menu for division
    :return:
    """
    print("---For division of 2 numbers(one must be a digit)----")
    base = input_and_check_base()
    nr_1 = input_and_check_number(base)
    nr_2 = input_and_check_number(base)
    return base, nr_1, nr_2

# ---- Addition ----
def addition(base, a, b):
    """
        Function for addition. Algorithm in pseudocode:
        c0=0; //c0, c1,… ,cn+1  Ԑ {0,1}  are the carries used in addition
        for i=0,n
            x’i(10) = xi(b) ;     y’i(10) = yi(b) ;    //convert the digits from base b in base 10
            s10 = x’i(10) + y’i(10) + ci(10) ;         //addition in base 10
            s’i(10) = s10 mod b ; ci+1 = s10 div b;
            si(b) = s’i(10);                  	       //convert the decimal value in base b
        end_for
        si+1 = ci+1;
    :param base: the base in which we are doing the addition (type: int)
    :param a: the first number(type: string)
    :param b: the second number(type: string)
    :return: the sum of a+b (type: string)
    """
    # Get the lengths of the 2 numbers
    len_a = len(a)
    len_b = len(b)
    # The sums will be strings
    s = ""
    summ = 0
    final_number = []

    # Fill with zeros the small number to make the numbers equal in length
    diff = abs(len_a - len_b)
    for i in range(1, diff + 1):
        s += "0"
    if len_a < len_b:  # Condition to check if the strings have lengths mis-match
        a = s + a
    else:
        b = s + b

    # Start the algorithm
    carry = 0
    index = max(len_a, len_b) - 1  # we start from right to left
    for i in range(index, -1, -1):
        # We transform the digits in base 10
        if a[i].isdigit():
            digit_a = ord(a[i]) - ord('0')
        else:  # in case it's a letter
            digit_a = ord(a[i]) - ord('0') - 7

        if b[i].isdigit():
            digit_b = ord(b[i]) - ord('0')
        else:  # in case it's a letter
            digit_b = ord(b[i]) - ord('0') - 7

        # Addition in base 10
        summ = int(digit_a) + int(digit_b) + int(carry)
        carry = summ // base
        digit = summ % base

        # we append to the list that represents the number
        if digit > 9:  #  if the digit is a letter
            final_number.append(chr(digit + ord('0') + 7))
        else:
            final_number.append(chr(digit + ord('0')))

    if carry:  # if we have a carry
        final_number.append(chr(carry + ord('0')))

    # reverse the number
    final_number.reverse()
    listToStr = ''.join(map(str, final_number))
    return listToStr


# ---- Subtraction ----
def subtraction(base, a, b):
    """
        Function for subtraction. Algorithm in pseudocode:
        c0=0; //c0, c1,… ,cn+1  Ԑ {0,1}  are the borrows used in subtraction
        for i=0,n
            x’i(10) = xi(b) ;     y’i(10) = yi(b) ;    //convert the digits from base b in base 10
            d10 = x’i(10) - y’i(10) - ci(10) ;         //subtraction in base 10
            ci+1 = 0 ;
            if (d10 < 0) then { d10 = d10+b ;  ci+1 = 1;}
            si(b) = s’i(10);                  	       //convert the decimal value in base b
        end_for
    :param base: the base in which we are doing the addition (type: int)
    :param a: the first number(type: string)
    :param b: the second number(type: string)
    :return: the sum of a+b (type: string)
    """
    # Get the lengths of the 2 numbers
    len_a = len(a)
    len_b = len(b)
    # The diff
    s = ""
    diff = 0
    final_number = []

    # invert the 2 numbers in case a < b
    if len_a < len_b:
        a, b = b, a
        len_a, len_b = len_b, len_a
    elif len_a == len_b:
        if a < b:
            a, b = b, a
            len_a, len_b = len_b, len_a

    diff_abs = abs(len_a - len_b)
    # Fill with zeros the small number to make the numbers equal in length
    for i in range(1, diff_abs + 1):
        s += "0"
    if len_a < len_b:  # Condition to check if the strings have lengths mis-match
        a = s + a
    else:
        b = s + b

    # Start the algorithm
    borrow = 0
    index = max(len_a, len_b) - 1  # we start from right to left
    for i in range(index, -1, -1):
        # We transform the digits in base 10
        if a[i].isdigit():
            digit_a = ord(a[i]) - ord('0')
        else:  # in case it's a letter
            digit_a = ord(a[i]) - ord('0') - 7

        if b[i].isdigit():
            digit_b = ord(b[i]) - ord('0')
        else:  # in case it's a letter
            digit_b = ord(b[i]) - ord('0') - 7

        # Subtraction in base 10
        d = int(digit_a) - int(digit_b) - int(borrow)
        borrow = 0
        if d < 0:
            d = d + base
            borrow = 1

        digit = d
        # we append to the list that represents the number
        if digit > 9:  #  if the digit is a letter
            final_number.append(chr(digit + ord('0') + 7))
        else:
            final_number.append(chr(digit + ord('0')))

    # In case we have 0s at the left of the number
    while len(final_number) != 1:
        if final_number[len(final_number)-1] == '0':
            final_number.pop(len(final_number)-1)
        else:
            break

    final_number.reverse()
    listToStr = ''.join(map(str, final_number))
    return listToStr


# ---- Multiplication ----
def multiplication(base, a, b):
    """
        a is always the number, and b is the digit
        Function for multiplication. Algorithm in pseudocode:
        c0=0; //c0, c1,… ,cn+1  Ԑ {0,1}  are the carries used in addition
        y’(10) = y(b) ;    //convert the digit from base b in base 10
        for i=0,n
            x’i(10) = xi(b) ;                          //convert the digits from base b in base 10
            p10 = x’i(10) * y’(10) + ci(10) ;         //multiplication in base 10
            p’i(10) = p10 mod b ; ci+1 = p10 div b;
            pi(b) = p’i(10);                  	       //convert the decimal value in base b
        end_for
        pi+1 = ci+1;
    :param base: the base in which we are doing the addition (type: int)
    :param a: the first number(type: string)
    :param b: the second number(type: string)
    :return: the sum of a+b (type: string)
    """
    # Swap the two numbers in case a is not the number
    if len(str(a)) < len(str(b)):
        a, b = b, a
    # In case it's not just one digit
    if len(b) != 1:
        raise ValueError("One number must have only 1 digit!")
    # The product
    product = 0
    final_number = []

    # Start the algorithm
    carry = 0
    # Transform b in base 10
    if b.isdigit():
        digit_b = ord(b) - ord('0')
    else:  # in case it's a letter
        digit_b = ord(b) - ord('0') - 7

    index = len(a) - 1  # we start from right to left

    for i in range(index, -1, -1):
        # We transform the digit in base 10
        if a[i].isdigit():
            digit_a = ord(a[i]) - ord('0')
        else:  # in case it's a letter
            digit_a = ord(a[i]) - ord('0') - 7

        # Multiplication in base 10
        product = int(digit_a) * int(digit_b) + int(carry)
        carry = product // base
        digit = product % base

        # we append to the list that represents the number
        if digit > 9:  #  if the digit is a letter
            final_number.append(chr(digit + ord('0') + 7))
        else:
            final_number.append(chr(digit + ord('0')))

    if carry:  # if we have a carry
        final_number.append(chr(carry + ord('0')))
    final_number.reverse()
    listToStr = ''.join(map(str, final_number))
    return listToStr


# ---- Division ----
def division(base, a, b):
    """
        a is always the number, and b is the digit
        Function for division. Algorithm in pseudocode:
        r = 0              //a decimal value
        y’(10) = y(b) ;    //convert the digit from base b in base 10
        for i=n,0,-1
            x’i(10) = xi(b) ;                //convert the digits from base b in base 10
            p10 = r * b + x'i(10) ;         //operations in base 10
            q’i(10) = p10 mod b ; r = p10 div b;
            qi(b) = q’i(10);                //convert the decimal value in base b
        end_for
        r(b) = r(10)
    :param base: the base in which we are doing the addition (type: int)
    :param a: the first number(type: string)
    :param b: the second number(type: string)
    :return: the sum of a+b (type: string)
    """
    # Swap the two numbers in case a is not the number
    if len(a) < len(b):
        a, b = b, a
    # In case it's not just one digit
    if len(b) != 1:
        raise ValueError("One number must have only 1 digit!")
    # The quotient and remainder
    q = 0
    r = 0
    final_number = []

    # Start the algorithm
    # Transform b in base 10
    if b.isdigit():
        digit_b = ord(b) - ord('0')
    else:  # in case it's a letter
        digit_b = ord(b) - ord('0') - 7

    index = len(a) - 1  # we start from left to right

    for i in range(0, index+1):
        # We transform the digit in base 10
        if a[i].isdigit():
            digit_a = ord(a[i]) - ord('0')
        else:  # in case it's a letter
            digit_a = ord(a[i]) - ord('0') - 7

        # Operation in base 10
        product = r * base + digit_a
        q = product // digit_b
        r = product % digit_b

        # we append to the list that represents the number
        if q > 9:  #  if the digit is a letter
            final_number.append(chr(q + ord('0') + 7))
        else:
            final_number.append(chr(q + ord('0')))

    if r > 9:  # if the remainder is a letter
        r = chr(r + ord('0') + 7)
    else:
        r = chr(r + ord('0'))

    while len(final_number) != 1:
        if final_number[0] == '0':
            final_number.pop(0)
        else:
            break

    listToStr = ''.join(map(str, final_number))
    return r, listToStr


# ---- Conversion from base 10 to another base ----
def from_ten(nr, base):
    """
    Converts given number nr, from base 10 to base b
    :param nr: the number that we need to convert(type: str)
    :param base: the base we convert the number (type:in)
    :return the converted number (type: str)
    """
    import string
    r = ''
    nr = int(nr)
    while nr > 0:
        # generate a string with numbers and letters, then select the digit that is the remainder
        r = string.printable[nr % base] + r
        nr //= base
    return r


# ---- Conversion from base to ten ----
def to_ten(nr, b):
    """
    Converts given number nr, from base b to base 10
    """
    return int(nr, b)


# ---- Successive divisions ----
def successive_divisions(base_start, nr, base_end):
    """
    We convert the number using the successive divisions method (for b<h)
    Steps:
        -the integer part is divided by the destination base (base_end) obtaining a quotient and a remainder
        -the quotient is divided by the destination base obtaining a new quotient and a new remainder
        ...
        -the process of successive divisions ends when 0 is obtained as a quotient
        -the remainders, in the reverse order of obtaining them, are the digits of the new representation in the destination base
    :param base_start: the actual base of the number (type: int)
    :param nr: the number we are converting (type: string)
    :param base_end: the base we want to convert to (type: int)
    :return: the converted number (type: string)
    """
    # In case one of the bases are 10
    if base_start == 10:
        return from_ten(nr, base_end)
    if base_end == 10:
        return to_ten(nr, base_start)

    if base_start < base_end:
        raise ValueError("For substitution method, you should use a source base bigger than the destination base!")

    # the remainders will be saved in a list
    remainders = []

    # we start the process of dividing
    r, q = division(base_start, nr, str(base_end))
    remainders.append(r)
    while q != '0':
        r, q = division(base_start, q, str(base_end))
        remainders.append(r)

    # reverse order of remainders
    remainders.reverse()
    listToStr = ''.join(map(str, remainders))
    return listToStr


# ---- Substitution method ----
def substitution_method(base_start, nr, base_end):
    """
    We convert the number using the substitution method (for b<h)
    Steps:
       -all the digits from the source representation are converted into the destination base
       -the base b is converted into the base h
       -we use the formula: N'(h) = a'0(h) * b'(h) ^ 0 + a'1(h) * b'(h) ^ 1 + ... + a'm(h) * b'(h) ^ m +
                                    + a'(-1)(h) * b'(h) ^ (-1) + ... + a'(-n)(h) * b'(h) ^ (-n)
       -since we only have natural numbers, we won't have negative powers
    :param base_start: the actual base of the number (type: int)
    :param nr: the number we are converting (type: string)
    :param base_end: the base we want to convert to (type: int)
    :return: the converted number (type: string)
    """
    # In case one of the bases are 10
    if base_start == 10:
        return from_ten(nr, base_end)
    if base_end == 10:
        return to_ten(nr, base_start)

    if base_start > base_end:
        raise ValueError("For substitution method, you should use a source base smaller than the destination base!")

    # we start with the products
    index = len(nr)-1

    # we save the products in a list1
    products = []
    base_start_power = "1"
    # we start from right to left
    for i in range(index, -1, -1):
        p = multiplication(base_end, str(nr[i]), str(base_start_power))
        base_start_power = multiplication(base_end, str(base_start), str(base_start_power))
        products.append(p)

    # we add the products
    sum = products[0]
    for i in range(1, len(products)):
        sum = addition(base_end, sum, products[i])
    return sum


# ---- Conversion using 10 as an intermediate base ----
def intermediate_base(base_start, nr, base_end):
    """
    We convert the number using base 10 as an intermediate base
    Steps:
       -conversion from source base to base 10 (using the substitution method)
       -conversion from base 10 into destination base (using the successive divisions method)
    :param base_start: the actual base of the number (type: int)
    :param nr: the number we are converting (type: string)
    :param base_end: the base we want to convert to (type: int)
    :return: the converted number (type: string)
    """
    decimal_number = substitution_method(base_start, nr, 10)
    final_number = successive_divisions(10, decimal_number, base_end)
    return final_number


# ---- Rapid conversions ----
def transform_binary_to_digit(group):
    """
    We transform the binary group to a digit
    :param group: the binary group (type:string)
    :return: the digit (type: str)
    """
    digit = 0
    power = 0
    for i in range(len(group)-1, -1, -1):
        digit += int(group[i]) * (2 ** power)
        power += 1

    final_digit = ""
    if digit > 9:  # if the digit is a letter
        final_digit = chr(digit + ord('0') + 7)
    else:
        final_digit = chr(digit + ord('0'))
    return str(final_digit)


def transform_digit_to_binary(digit, exponent):
    """
    Transform the digit into a binary group
    :param digit: the digit (type: str)
    :param exponent: the number of digits in a group (type: int)
    :return: the binary group (type:
    """
    # we start making the binary groups for every digit
    binary_group = []
    while digit:
        binary_group.append(str(digit % 2))
        digit //= 2

    # fill with 0s where it's needed
    while len(binary_group) != exponent:
        binary_group.append("0")

    # reverse it and make it a string
    binary_group.reverse()
    listToStr = ''.join(map(str, binary_group))
    return listToStr


def convert_to_binary(nr, exponent):
    """
    Convert the number to binary
    :param nr: the number (type:string)
    :param exponent: the number of digits in a group (type: int)
    :return: the number converted in binary (type: str)
    """
    number_in_binary = []
    for i in range(len(nr)):
        if nr[i].isdigit():  # digit in base 10
            digit = ord(nr[i]) - ord('0')
        else:  # in case it's a letter
            digit = ord(nr[i]) - ord('0') - 7

        binary_group = transform_digit_to_binary(digit, exponent)

        # put it in the final number which is a string
        number_in_binary.append(binary_group)

    number_final = ''.join(map(str, number_in_binary))
    return number_final


def convert_to_base(number_binary, exponent):
    """
    Convert the binary number to destination base
    :param number_binary: the number in base 2 (type: str)
    :param exponent: the number of digits in a group (type: int)
    :return: the number converted
    """
    exponent = 0 - exponent
    result = ""

    # we convert from binary to our final base
    for i in range(len(number_binary), -1, exponent):
        binary_group = number_binary[(exponent + i):i]

        # fill with 0s where we need
        if i < (0-exponent):
            if i == 0:
                break
            binary_group = []
            nr_zero = 0 - exponent - i
            print(nr_zero)
            while nr_zero > 0:
                binary_group.append("0")
                nr_zero -= 1
            for j in range(i):
                binary_group.append(number_binary[j])
                #i -= 1
            listToStr = ''.join(map(str, binary_group))
            binary_group = listToStr
        digit = transform_binary_to_digit(binary_group)
        result += digit

    # reverse the string
    result = result[::-1]
    return result


def rapid_conversions(base_start, nr, base_end):
    """
    We use rapid conversions
    From small to big:
       -Each digit from the source number in base p=2^k will be replaced by the corresponding group of k binary digits
        (adding if it is necessary insignificant zeros to the left).
    From big to small:
       -for the integer part: from right to left make groups of k binary digits (eventually we add to the left
        insignificant zeros to have a complete group)
       -the groups will be replaced by the corresponding digits in base q=2^k
    :param base_start: the actual base of the number (type: int)
    :param nr: the number we are converting (type: string)
    :param base_end: the base we want to convert to (type: int)
    :return: the converted number (type: string)
    """
    if base_start not in [2, 4, 8, 16] or base_end not in [2, 4, 8, 16]:
        raise ValueError("For rapid conversions, the base should be equal to 2, 4, 8 or 16")

    # the k binary digits
    import math
    exponent_start = math.log2(base_start)
    exponent_end = int(math.log2(base_end))

    # we convert the number to binary
    if base_start != 2:
        number_binary = convert_to_binary(nr, exponent_start)
    else:
        number_binary = nr

    # we convert from binary to our final base
    result = convert_to_base(number_binary, exponent_end)

    return result


def menu_conversions(base_start, nr, base_end):
    """
    The menu for conversions
    :param base_start: the actual base of the number (type: int)
    :param nr: the number we are converting (type: string)
    :param base_end: the base we want to convert to (type: int)
    :return: the converted number (type: string)
    """
    print("\nb = source base, h = destination base")
    print("Choose method:")
    print("1.1 Method of successive division (h<b)")
    print("1.2 Substitution method (b<h)")
    print("1.3 Conversion using 10 as an intermediate base")
    print("1.4 Rapid conversions (executable form) between two bases p,q={2, 4, 8, 16}")
    option = input("\nInsert option: ")
    if option == "1.1":
        print(successive_divisions(base_start, nr, base_end))
    if option == "1.2":
        print(substitution_method(base_start, nr, base_end))
    if option == "1.3":
        print(intermediate_base(base_start, nr, base_end))
    if option == "1.4":
        print(rapid_conversions(base_start, nr, base_end))


def start():
    unicorns_exist = True
    while(unicorns_exist):
        option = input("\nInsert option: ")
        if option == "1":
            try:
                base_start, nr, base_end = input_bases_and_numbers()
                menu_conversions(base_start, nr, base_end)
            except ValueError as error:
                print(error)
        elif option == "2":
            try:
                base, nr_1, nr_2 = input_and_print_menu_addition()
                print(addition(base, nr_1, nr_2))
            except ValueError as error:
                print(error)
        elif option == "3":
            try:
                base, nr_1, nr_2 = input_and_print_menu_subtraction()
                print(subtraction(base, nr_1, nr_2))
            except ValueError as error:
                print(error)
        elif option == "4":
            try:
                base, nr_1, nr_2 = input_and_print_menu_multiplication()
                print(multiplication(base, nr_1, nr_2))
            except ValueError as error:
                print(error)
        elif option == "5":
            try:
                base, nr_1, nr_2 = input_and_print_menu_division()
                r, q = division(base, nr_1, nr_2)
                print("quotient = ", q)
                print("remainder = ", r)
            except ValueError as error:
                print(error)
        elif option == "exit":
            unicorns_exist = False
        else:
            print("Oops!!! Wrong command")



if __name__ == '__main__':
    print_menu()
    start()
