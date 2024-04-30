import json



class ClassCodeGenerator:
    @staticmethod
    def  generate_class(jshon_data):
        class_name = jshon_data[ "class_name"]
        attributes = jshon_data["attributes"]
        methods = jshon_data["methods"]


        code = f"class {class_name}:\n"

        for attr in attributes:
            code += f"      {attr["name"]}:{attr["type"]}\n"

        code += "\n"
        # Aici urmeaza sa generam definitiile functiilor
        for meth in methods:
            args = ", ".join(meth["args"])
            code += f"  def{meth["name"]}(self, {args}):"
            if meth["return_type"] != "None":
                code += f"  -> {meth["return_type"]}"
            code += "\n"
            code += f"      {meth["body"]}\n"

        return  code

def main():
    with open("recap.json", "r") as file:
        json_data = json.load(file)
    generated_code = ClassCodeGenerator.generate_class(json_data)
    print(generated_code)
    # TODO: scrieti codul intr-un fisier separat .py (intrfata_mea.py)




if __name__ == "__main__":
    main()

