def moyenne(args):
    somme = 0
    for i in args:
        somme += i
    return somme / len(args)


try:
    with open("data-files/students.txt") as file:
        list_students = []
        list_students_moyenne = []
        for line in file:
            if list_students.count(line.rstrip()[:-3]) == 0 and line != "\n":
                list_students.append(line.rstrip()[:-3])

        print(list_students)
        for student in list_students:
            list_result = []
            print(student)
            print(line.rstrip())
            for lignes in file:
                print('ici')
                print(lignes.rstrip())
except FileNotFoundError:
    print("pas trouve")
except IOError:
    print('Erreur IO.')
