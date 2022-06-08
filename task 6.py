# 1.  Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

# w = 1
# x = 2
# y = 3
# z = 0
# z = (w+x) * y;   
# print(z)

# 2 Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, 
# а втором файлике — сжатая версия этого текста).

# with open('42_RLE1_decoded.txt', 'r') as data:
#     my_text = data.read()

# def encode_rle(ss):
#     str_code = ''
#     prev_char = ''
#     count = 1
#     for char in ss:
#         if char != prev_char:
#             if prev_char:
#                 str_code += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     return str_code

            
# str_code = encode_rle(my_text)
# print(str_code)

# with open('42_RLE2_encoded.txt', 'r') as data:
#     my_text2 = data.read()

# def decoding_rle(ss:str):
#     count = ''
#     str_decode = ''
#     for char in ss:
#         if char.isdigit():
#             count += char 
#         else:
#             str_decode += char * int(count)
#             count = ''
#     return str_decode

# str_decode = decoding_rle(my_text2)
# print(str_decode)

# 3 ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите. ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 . Если в строку включены числа или специальные символы, они должны быть возвращены как есть. Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
# Не использовать функцию encode.
# dict1 = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5,
#         'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10,
#         'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15,
#         'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20,
#         'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}

# dict2 = {0 : 'Z', 1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D', 5 : 'E',
#         6 : 'F', 7 : 'G', 8 : 'H', 9 : 'I', 10 : 'J',
#         11 : 'K', 12 : 'L', 13 : 'M', 14 : 'N', 15 : 'O',
#         16 : 'P', 17 : 'Q', 18 : 'R', 19 : 'S', 20 : 'T',
#         21 : 'U', 22 : 'V', 23 : 'W', 24 : 'X', 25 : 'Y'}
# def encrypt(message, shift):
#     cipher = ''
#     for letter in message:
#         if(letter != ' '):
#             num = (dict1[letter] + shift ) % 26
#             cipher += dict2[num]
#         else:
#             cipher += ' '
#     return cipher
# def decrypt(message, shift):
#     decipher = ''
#     for letter in message:
#         if(letter != ' '):
#             num = ( dict1[letter] - shift + 26) % 26
#             decipher += dict2[num]
#         else:
#             decipher += ' '
#     return decipher
# def main():
#     message = "GEEKS FOR GEEKS"
#     shift = 13
#     result = encrypt(message.upper(), shift)
#     print (result)
#     message = "TRRXF SBE TRRXF"
#     shift = 13
#     result = decrypt(message.upper(), shift)
#     print (result)
# if __name__ == '__main__':
#     main()