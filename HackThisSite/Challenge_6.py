import string

string_input = input("Type your string: ")
str_to_char = list(string_input)

print(str_to_char)

print("1st string: "+ str_to_char[1])
print("2nd string: "+ str_to_char[2])
print("3rd string: "+ str_to_char[3])
print("4th string: "+ str_to_char[4])
print("5th string: "+ str_to_char[5])
print("6th string: "+ str_to_char[6])
print("7th string: "+ str_to_char[7])

char_to_ord=ord(str_to_char[1])
char_to_ord2=ord(str_to_char[2])
char_to_ord3=ord(str_to_char[3])
char_to_ord4=ord(str_to_char[4])
char_to_ord5=ord(str_to_char[5])
char_to_ord6=ord(str_to_char[6])
char_to_ord7=ord(str_to_char[7])
print(f'The ascii value of the first letter is: {char_to_ord}')
char_to_ord-=1
char_to_ord2-=2
char_to_ord3-=3
char_to_ord4-=4
char_to_ord5-=5
char_to_ord6-=6
char_to_ord7-=7

print(chr(char_to_ord))
print(chr(char_to_ord2))
print(chr(char_to_ord3))
print(chr(char_to_ord4))
print(chr(char_to_ord5))
print(chr(char_to_ord6))
print(chr(char_to_ord7))

final = str_to_char[0] + chr(char_to_ord) + chr(char_to_ord2) + chr(char_to_ord3) + chr(char_to_ord4) + chr(char_to_ord5) + chr(char_to_ord6) + chr(char_to_ord7)

#Got a little bit bored and decided to write it in Python. I initially thought that it was a Caesar Cipher encryption though but apparently, it wasn't.
#

print(final)



