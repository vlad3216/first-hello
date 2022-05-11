print('Добро пожаловать в шифратор/дешифратор для шифра Цезаря.')
t = input('Введите "1" для шифрования, "2" для дешифрования: ')
a = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
if t == '1':
       s = input('Введите текст (только буквы [a-z, A-Z]): ')
       key = int(input('Введите ключ сдвига: '))
       caesar = ""
       for letter in s:
              position = a.find(letter)
              npos = position + key
              if letter in a:
                  caesar = caesar + a[npos]
              else:
                  caesar = caesar + letter
       print('Результат:', caesar)

elif t == '2':
    s = input('Введите текст (только буквы [a-z, A-Z]): ')
    key = int(input('Введите ключ сдвига: '))
    caesar = ""
    for letter in s:
        position = a.find(letter)
        npos = position - key
        if letter in a:
            caesar = caesar + a[npos]
        else:
            caesar = caesar + letter
    print('Результат:', caesar)
