


import re
text = 'Sunt Alex si studiez Python studiez.'

pattern = r'studiez'

gasit = re.findall(pattern, text)
print(gasit)


text2 = "The cat sat sat on the mat"
pattern2 = r"\b\w{3}\b"
gasit2 = re.findall(pattern2, text2)
print(gasit2)

