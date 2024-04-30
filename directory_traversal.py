# se cere un script python care traverseaza un director, listeaza toate fisierele de tip text!, printand numele
# fisierului si prima linie cu continutul acesteia

import os
import linecache


def traverse_directory(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                print(f"{file}")
                with open(os.path.join(root, file), 'r') as f:
                    print(f"Prima linie este {f.readline()}")


# traverse_directory("C:\\Users\\ilies\\OneDrive\\Desktop\\SDA\\Test")

def traverse_directory_non_recursive(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if (entry.is_file() and entry.name.endswith('.txt')):
                print(f'Fisierul: {entry.name}.')


# traverse_directory_non_recursive("C:\\Users\\ilies\\OneDrive\\Desktop\\SDA\\SDA Python - intermediate")


def read_multi_lines(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                print(f"{file}")
                with open(os.path.join(root, file), 'r') as f:
                    # for _ in range(2):
                    #     print(f.readline().strip())
                    linia_2 = linecache.getline(f.name, 3).strip()
                    print(linia_2)
                    # lines = f.readlines()
                    # for line in lines:
                    #     print(line.strip())
                    '''
                    while True:
                        line = f.readline()
                        if not line:
                            break
                        print(line.strip())
                    '''


read_multi_lines("C:\\Users\\ilies\\OneDrive\\Desktop\\SDA\\Test")

# dat fiind un fisier, de orice tip, care contine mai multe linii
# se cere crearea unei clase ce introduce fiecare linie intr-o structura de date alease de voi
# lista sau dictionar
# astfel incat atunci cand vrem sa accesam o linie, sa o putem face dupa index/cheie
# tratati posibilele exceptii