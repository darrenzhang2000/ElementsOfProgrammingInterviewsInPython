'''
Hello Worl  d  !
0123456789 10 11

e _ l
1 5 9

H l o W r d
0 2 4 6 8 10

l o !
3 7 11
'''

def snakeString(s):
    top = []
    mid = []
    bot = []
    for i, c in enumerate(s):
        if i % 2 == 0:
            mid.append(c)
        elif i % 4 == 1:
            top.append(c)
        else:
            bot.append(c)
    return "".join(top + mid + bot)

print(snakeString('Hello World!'))

def snakeString2(s):
    return s[1::4] + s[::2] + s[3::4]

print(snakeString2('Hello World!'))
            