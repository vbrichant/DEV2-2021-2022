import string


def nb_divisors(an_integer):
    list_divisors = []
    for i in range(an_integer + 1):
        if i != 0 and an_integer % i == 0:
            list_divisors.append(i)
    return len(list_divisors)


# nb_divisors(6)


def perfect_square(an_integer):

    for i in range(an_integer + 1):
        if i != 0 and (an_integer / i).is_integer():
            if (i != an_integer or i == 1) and (an_integer / i) == i:
                return True
    return False


print(perfect_square(1))


def file_extension(a_string):
    if len(a_string) >= 4 and a_string[-4] == ".":
        return a_string[-3:]
    else:
        return ""


print(file_extension("ere.tes"))
print(file_extension("ere.tess"))
print(file_extension(".tes"))
print(file_extension("tes"))


def is_strong_password(a_string):
    num = False
    alpha = False
    cara_speciaux = False
    for i in range(len(a_string)):
        if a_string[i].isnumeric():
            num = True
        if a_string[i].isalpha():
            alpha = True
        if not a_string[i].isnumeric() and not a_string[i].isalpha():
            cara_speciaux = True
    if cara_speciaux and num and alpha and len(a_string) >= 12:
        return True
    return False


is_strong_password("testing123@@")
is_strong_password("testing1238@@#")
is_strong_password("testing13@@")
is_strong_password("test@@")
is_strong_password("123@@")
