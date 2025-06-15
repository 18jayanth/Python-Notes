import re
s='This is Harshad And Ashu'
print(re.findall(r'\bTh',s)) #['Th'] beginning Th
print(re.findall(r'\bTh\b',s))#[]    'Th' is not a seperate word
print(re.findall(r'Th\b',s)) #[]     ending Th
print(re.findall(r'\bis',s))#['is]    beginning with 'is'
print(re.findall(r'is\b',s))#['is','is'] ending with 'is'
print(re.findall(r'\bis\b',s))#['is']   'is' is a seperate word
print(re.findall(r'\bThis\b',s))#['This']  'This' is a seperate word
print(re.findall(r'is\B',s))#[]        ending should not be 'is'
print(re.findall(r'\Bis',s)) #['is']   starting should not be 'is' so only 'is' from 'This'
print(re.findall(r'\Bis\B',s))#[]   it matches only if completely inside a word (no word boundary on either sides)

s='19.98'
print(re.search(r'\d+[.]\d+',s))
#<re.Match object; span=(0, 5), match='19.98'>
mo=re.search(r'(\d+)[.](\d+)',s) #divided into groups
print(mo.groups())          #('19', '98')
mo=re.search(r'(\d+)([.])(\d+)',s) #divided into groups
print(mo.groups())          #('19','.','98')

s='This is Harshad and Ashu'
#it divides according to white spaces
print(re.split(r'\s',s))  #['This', 'is', 'Harshad', 'and', 'Ashu']
print(re.split(r'\s',s,2)) #['This', 'is', 'Harshad and Ashu']
print(re.sub(r'\s','#',s))# This#is#Harshad#and#Ashu it replaces white spaces with'#'


po=re.compile(r'\s') #this will create a pattern which we can use
print(po.findall(s)) #[' ', ' ', ' ', ' ']


io=re.finditer('\s',s)
print(io) #<callable_iterator object at 0x0000017520892BC0>
for i in io:
    print(i)
# <re.Match object; span=(4, 5), match=' '>
# <re.Match object; span=(7, 8), match=' '>
# <re.Match object; span=(15, 16), match=' '>
# <re.Match object; span=(19, 20), match=' '>

s='hai harshad there are my numbers 8985338755 7330730901 123345678'
print(re.findall(r'[6-9]\d{9}',s)) #['8985338755', '7330730901'] any number starts with 6,7,8,9 followed by 9 numbers

s='hai harshad there are my numbers +91-8985338791 7330730901 +91-123345672'
print(re.findall(r'[+]91-[6-9]\d{9}',s)) #['+91-8985338791']starts with +91- and next 6,7,8,9 followed by 9 numbers

s='hai python and django1234 h'
print(re.findall('h',s))  #['h','h','h']
print(re.findall('[h]',s)) #['h', 'h','h']
print(re.findall('and',s)) #['and']
print(re.findall('[and]',s)) #['a', 'n', 'a', 'n', 'd', 'd', 'a', 'n']
print(re.findall('[abcdef]',s))#['a', 'a', 'd', 'd', 'a']
print(re.findall('[a-z]',s)) #['h', 'a', 'i', 'p', 'y', 't', 'h', 'o', 'n', 'a', 'n', 'd', 'd', 'j', 'a', 'n', 'g', 'o', 'h']

s='Hai Python And Django1234'
print(re.findall('[a-z]',s))#['a', 'i', 'y', 't', 'h', 'o', 'n', 'n', 'd', 'j', 'a', 'n', 'g', 'o']
print(re.findall('[a-zA-Z]',s)) #['H', 'a', 'i', 'P', 'y', 't', 'h', 'o', 'n', 'A', 'n', 'd', 'D', 'j', 'a', 'n', 'g', 'o']
print(re.findall('[a-zA-Z0-9]',s))#['H', 'a', 'i', 'P', 'y', 't', 'h', 'o', 'n', 'A', 'n', 'd', 'D', 'j', 'a', 'n', 'g', 'o', '1', '2', '3', '4']
print(re.findall('[a-zA-Z0-9][a-zA-Z0-9]',s))#['Ha', 'Py', 'th', 'on', 'An', 'Dj', 'an', 'go', '12', '34']
print(re.findall('[a-zA-Z0-9]{2}',s))#['Ha', 'Py', 'th', 'on', 'An', 'Dj', 'an', 'go', '12', '34']
print(re.findall('[a-zA-Z0-9]{4}',s))#['Pyth', 'Djan', 'go12']
print(re.findall(r'[2-5][0-9]', s))#['23']
print(re.findall('\d+',s))#['1234']








