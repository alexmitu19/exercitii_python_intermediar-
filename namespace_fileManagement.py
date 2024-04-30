class FileManager:
    # def __init__, __enter__, __exit__
    def __init__(self, file_name, mod):
        self.mod = mod
        self.file_name = file_name
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mod)
        # print("AM intrat!")
        # ...
        return self.file

    def __exit__(self, exc_type, exc_val,
                 exc_tb):  # exc_type -> type, exc_value -> valoarea curenta, exc_tb ->traceback
        # ...
        self.file.close()
