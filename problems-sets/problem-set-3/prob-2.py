""" 2. Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|> """
Name=input()
Date=input()
#print(f"letter=''' \nDear {Name} ,\n You are selected!\n{Date}  ''' ") one way
letter = '''
Dear <|Name|>,
You are selected!
<|Date|> '''
print(letter.replace("<|Name|>",Name).replace("<|Date|>",Date))

