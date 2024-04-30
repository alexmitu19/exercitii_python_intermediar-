class Oarecare:
    lista_mea = [] # este variabila comuna instantei clasei Oarecare # sau variabila globala a instantei clasei, shared!!!! de obiecte

    def __init__(self, item: str):
        self.lista_mea.append(item)

    @classmethod
    def get_list(cls):
        return cls.lista_mea

    @classmethod
    def create_with_item(cls, item):
        return cls(item)  # echivalent cu ob = Oarecare(5)

    @staticmethod
    def get_list_length():
        return len(Oarecare.lista_mea)


#o1 = Oarecare("123")
#Oarecare.create_with_item("345")
#o2 = Oarecare(5)
#o3 = Oarecare(238)


#  o1.create_with_item obiectul o1 este alocat : create with item, get list ,lista mea;
print(Oarecare.get_list())
print(Oarecare.get_list_length())