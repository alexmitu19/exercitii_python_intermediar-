from namespace_fileManagement import FileManager


class ConvertFileDict:
    def __init__(self, file_name):
        self.file_name = file_name
        self.dict_linii = {}
        self._read_file()

    # I/O sau get/set
    def _read_file(self):
        with FileManager(self.file_name, "r") as file:
            for index, line in enumerate(file):
                self.dict_linii[index] = line.strip()

    def get_line_by_index(self, index):
        return self.dict_linii.get(index, None)


o1 = ConvertFileDict("gg.txt")


# print(o1.get_line_by_index(1))


class ConvertFileList:
    def __init__(self, filename):
        self.filename = filename
        self.lista_linii = []
        self._read_file()

    def _read_file(self):
        with FileManager(self.filename, 'r') as file:
            for line in file:
                self.lista_linii.append(line.strip())

    def get_line_by_index(self, index):
        if 0 <= index < len(self.lista_linii):
            return self.lista_linii[index]
        else:
            return None


o2 = ConvertFileList("exemplu1.txt")
print(o2.get_line_by_index(3))

'''
dict vs lista

O(n) : complexitatea de calcul

{
O(n) ; complexitate liniara
}
for i in range(n): -> O(n) 
for i in range(n):
    for j in range(m): O(n^2)
get -> O(1) - constant

dict -> structurat ca un arbore ( get -> O(1) )

lista -> zona contigua de memorie ( continuu de memorie ) 
parcurgi element cu element : O(n)
'''