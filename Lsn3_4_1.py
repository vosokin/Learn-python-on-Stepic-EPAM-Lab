'''
Напишите программу, которая считывает из файла строку, соответствующую тексту,
сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
'''
def decode(string):
    result, digit = '', ''
    for char in string:
        if char.isdigit():
            digit += char
            if digit:
                result += letter * int(digit)
                digit = ''
        elif char.isalpha():            
            letter = char            
    return result
