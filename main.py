def move(s):
    ch = ""
    for i in s.split():
        for j in i:
            if j == 'я':
                j = 'а'
            elif j == 'Я':
                j = 'А'
            else:
                j = chr(ord(j)+1)
            ch += j
            print(j)
        ch += " "
    return ch
print(move("АбВгЯя фы ыы"))