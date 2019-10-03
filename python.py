import keyword
print(keyword.kwlist)
#test strings
string ='hello_world'
print(string)
len(string )
print(string[-2])
print(string[-6])
print(string[:5])
print(string[3:8])# from 4 th character to 7 th character 8 th character is excluded from the list
print(string[:5])#prints 5 characters from the start
print(string[5:])
str1=2*('Con'+'catination')
print(str1)
t='Ford'
print('L'+t[1:])
#using format methods
print("today I had {0} cups of {1}".format(0,'Milk'))#positional arguments
print('prices: ({x},{y},{z})'.format(x=2.0,y=3.0,z=9.0))#keyword arguments
print("the {vehicle} ahd {0} crashes in {1} months".format(5,6,vehicle='truck') )
#using the format method for indentation
print('{:<20}'.format('text'))#left indentation
print('{:>20}'.format('text'))#right indentation
print('{:>2}'.format('text'))#right indentation
#conversion to binary ,hexadecimal and octal form of a given number
print('binary form is {:b}  '.format(21))
print('hexadecimal from of 21 is {:x}  '.format(21))
print('octal form of 21 is {:o}  '.format(21))
print("I'm a string in python")
print("hello I\"m  a string in python ")
print(r'c:\number\nan')#using r before the print statement would avoid the escape sequence character
# to print the exact format of the way the way it is printed tin the terminal use """\ text pattern """
print("""\
Hello World 
    welcome
            to 
            Python tutorial
            """)
#operator precedence
#not
#and
#OR

d=5
e=1
f=False
g='python'
h='some'
z=not((not(e<=d) and (g>=h))or f ) and 1
print(z)
print("(g>=h)",(g>=h))
#if condition
p ='hi'
if p =='hello':
    print("Hi,How are you?")
elif p=='hi':
    print("Hry There!")
else:
    print("Hey!")
    # terary operator using If
ps=""
me="Hi" if ps=="Hello" or ps=="Hi"  else "hey"
print(me)

#loop in python
for i in range (1,10,3):
    print(i)
st="string traversal"
for i in range(len(st)):
    print(st[i])
for char in st:
    print(char)
print("endddddddddddddddddd")
for i in range(3):
    for j in range(2):
        print(j)
# printing multiplication table
print("printing multiplication table ")
for i in range(1,11):
    print('{:<4}|'.format(i),end="")
    for j in range(1,11):
        print('{:>4}'.format(i*j),end="")
    if i==1:
        print('\n{:#^45}'.format(""),end="")
    print("")

# while statement
condition=10
while condition !=0:
    print(condition)
    condition=condition-1
#break
while True:
    print("infinite")
    break
#continue
for i in range (1,11):
    if i==5:
        continue
    print(i)
