import re

texto = '''Hola Mundo.
Me gusta Python!!!!!
Mi primer numero de la suerte es 987-654-321
Mi segundo numero de la suerte es 876-543-210
Mi tercer numero de la suerte es 765-432-100
Mi cuarto numero de la suerte es 123-456-123-123-456
'''
 

#************ METACARACTERS ************
# \d	- Digits (0-9)
print(re.search(r'\d', texto)) # get the first digit
print(re.findall(r'\d', texto)) # get all digits

# \D 	- No Digits (0-9)
print(re.findall(r'\D', texto, flags=re.DOTALL)) # get NO digits

# \w	- Caracter (a-z, A-Z, 0-9, _)
print(re.findall(r'\w', texto)) # getting caracters and numbers only

# \W	- No Caracters
print(re.findall(r'\W', texto)) # getting no caracters and numbers

# \s	- Blank space (space, tab, new line)
print(re.findall(r'\s', texto)) # getting spaces and new lines

# \S	- No blank space (space, tab, new line)
print(re.findall(r'\S', texto)) # getting everything and ignoring spaces and new lines

# .	- Whatever caracter except new line
print(re.findall(r'.', texto)) # getting everything except new lines

# \	- Cancell special caracters
print(re.findall(r'\.', texto))

# ^	- Start with a specific line string
print(re.findall(r'^Hola', texto))

# $	- End in a string
print(re.findall(r'Mundo.$', texto, flags=re.M)) # re.M, multi lines


#************ CARACTERS NUMBERS ************
# *	- 0 or more
print(re.findall(r'Python!*', texto))

# +	- 1 or more
print(re.findall(r'Python!+', texto))

# ?	- 1 or 0
print(re.findall(r'Python!?', texto)) # take or no take

# {3}	- find an exact number of elements
print(re.findall(r'Python!{2}', texto)) # take or no take

# {n,}	- Number range(Min, Max)
print(re.findall(r'Python!{2,}', texto)) # take or no take

# {3,4}	- Number range(Min, Max)
print(re.findall(r'Python!{2,3}', texto)) # take or no take

# Exercise: -digits-
print(re.findall(r'-\d*-', texto))

# Exercise: digits-digits-digits
print(re.findall(r'(\d*)(-\d*-)(\d*)', texto))

# ( )	- Groups
print(re.findall(r'(\d*)(-\d*-)(\d*)', texto))

# []	- Find caracters : [a-dA-D0-9]
print(re.findall(r'[98]\d{2}', texto))
print(re.findall(r'[a-z]', texto))
print(re.findall(r'[a-zA-Z]', texto))
print(re.findall(r'[a-dA-D0-9]', texto))

# [^ ]	- Find negative of a caracters: [^a-d] --everything except from a to d
print(re.findall(r'[^a-d]', texto))

# |	- concat flags

# \b	- Word limit : .\b right limit
print(re.findall(r'.\b', texto))

# \B	- Without limit 
print(re.findall(r'.\B', texto))

# \1	- Reference
print(re.findall(r'(123-)\1', texto))


# EXERCISES AND FLAGS
print(re.findall(r'^hola', texto, flags=re.I)) # re.I : ignore 

print(re.findall(r'[^\w\s]', texto))

# check a date
dates = '''
13-04-2021
2021-13-04
2021-04-13
'''
print(re.findall(r'\d{2}-\d{2}-\d{4}', dates))

# check user
# 4-14 and only numbers or words
info = '''
user10
abc
10
'''
print(re.findall(r'[a-z0-9]{4,14}', info))