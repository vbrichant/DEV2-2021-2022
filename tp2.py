from filecmp import cmp

char_to_dots = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '&': '.-...',
                "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.', ':': '---...', ',': '--..--', '=': '-...-',
                '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'}


def morse_encode(to_be_translated):
    translation = ""
    for i in range(len(to_be_translated)):
        print(to_be_translated[i])
        if to_be_translated[i] == " ":
            translation += ""
        if to_be_translated[i].isalpha():
            for u in char_to_dots:
                if u == to_be_translated[i].upper():
                    translation += char_to_dots[u]
        else:
            for u in char_to_dots:
                if u == to_be_translated[i]:
                    translation += char_to_dots[u]
        translation += "/"

    return translation
print(morse_encode('Vive Python !'))
print('...-/../...-/./ /.--./-.--/-/..../---/-./ /-.-.--/')

# '...-/../...-/./ /.--./-.--/-/..../---/-./ /-.-.--/'
# '...-/../...-/./ /.--./-.--/-/..../---/-./ /-.-.--/'

grades = {'HE31337': 3, 'HE31737': 9, 'HE31722': 9, 'HE31347': 5, 'HE31837': 16, 'HE424242': 17, 'HE696969': 17, 'HE201583': 16}


def grade_position(all_grades, student_id):
    position = 1
    cotes_en_simple = []
    for y in all_grades:
        if all_grades[y] not in cotes_en_simple:
            cotes_en_simple.append(all_grades[y])
    cotes_en_simple.sort(reverse=True)
    for i in all_grades:
        if student_id == i:
            for u in cotes_en_simple:
                if u == all_grades[i]:
                    return position
                if u > all_grades[i]:
                    position += 1
    return 0

print(grade_position(grades, 'HE31337'))
list_of_tuple_test = [('Jean', 33), ('Martin', 11), ('Tom', 42), ('Vincent', 72)]


def sort_on_length(list_of_tuple, name_index=0):
    return sorted(list_of_tuple, key=lambda x: len(x[name_index]))


votes_recolte = ['T1031', 'T1031', 'T1031', 'T1031', 'T1031', 'T1031', 'T1031', 'T1031', 'T1031', 'T1031', 'T1031',
                 'T1031',
                 'T1031', 'T2112', 'T2112', 'T2112', 'T2112', 'T1031', 'T1031', 'T1031', 'T1234', 'T1234', 'T1235',
                 'T1234']


def find_winner(votes):
    if votes.__len__() == 0:
        return ''
    result = {}
    for i in votes:
        trouve = False
        for u in result:
            if u == i:
                trouve = True
                temp = {u: result[u] + 1}
                result.update(temp)
        if not trouve:
            result[i] = 1
    sorted(result.items(), key=lambda x: x[1])
    return list(result.keys())[0]


def arguments_analysis(*args):
    compteur = 0
    meme_type = True
    type_precedant = None
    for i in args:
        compteur += 1
    for e in args:
        if e == args[0]:
            type_precedant = type(e)
        if type(e) != type_precedant and e != args[0]:
            meme_type = False
            return compteur, meme_type
        else:
            type_precedant = type(e)
    return compteur, meme_type


print(morse_encode("abc157@"))

print(sort_on_length(list_of_tuple_test))
print(find_winner(votes_recolte))
nb_args, same_type = arguments_analysis('a', 42, {1, 2, 3})
print(nb_args)
print(same_type)
