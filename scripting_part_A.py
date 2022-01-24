import argparse
import json


def question1():
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the sum')
    args = parser.parse_args()
    print(sum(args.integers))


def question2():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str,
                        help='name of the file')
    args = parser.parse_args()
    print(args)
    try:
        with open(args.file) as file:
            maximum = 0
            for line in file:
                for word in line.rstrip().split():
                    if word.isnumeric():
                        if maximum < int(word):
                            maximum = int(word)
            print(maximum)
    except FileNotFoundError:
        print('Fichier introuvable.')
    except IOError:
        print('Erreur IO.')


def question3():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type=str, help="le json d'entré")
    parser.add_argument('--output_file',
                        help="le json de sortie (param optionel: si omis, alors le fichier d'entrée sera utilisé)")
    parser.add_argument('--filter_teacher', type=str, help="le json d'entré")
    parser.add_argument('--filter_good', help="le json d'entré")
    parser.add_argument('--order', type=str, help="le json d'entré")
    parser.add_argument('--select', type=str, nargs='*', help="le json d'entré", choices=["ID",
                                                                                          "Name",
                                                                                          "Gender"
                                                                                          "Class",
                                                                                          "Seat",
                                                                                          "Teacher",
                                                                                          "Course",
                                                                                          "Grade",
                                                                                          "Info"])
    args = parser.parse_args()
    final_json = []
    print(args)
    if args.input_file:
        try:
            with open(args.input_file) as file:
                data_json = json.load(file)
                for data in data_json:
                    if args.filter_teacher and data['Teacher'] == args.filter_teacher:
                        new_json = {}
                        print(data)
                    if args.filter_good:
                        print(data)
                    if args.select:
                        for i in args.select:
                            print(i)
        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')


if __name__ == '__main__':
    question3()
