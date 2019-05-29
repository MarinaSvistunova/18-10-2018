# NUMBER 1
def is_digit(string):
    if string.isdigit():
       return int(string)
    else:
        try:
            float(string)
            return float(string)
        except ValueError:
            return False
def culc(strForCulc):
    outp = strForCulc
    str2 = list(strForCulc)
    operators ={
        '+': (lambda x, y: x + y),
        '-': (lambda x, y: x - y),
        '*': (lambda x, y: x * y),
        '/': (lambda x, y: x / y),
        '^': (lambda x, y: x ** y)
    }
    operators2 = {
        '+': 'addition',
        '-': 'subtraction',
        '*': 'multiplication',
        '/': 'division',
        '^': 'exponentiation'
    }
    operator = ''
    num = ''
    for i in str2:
        if i in '0123456789.' and operator == '':
            num += i
        elif operator == '':
            x = int(num)
            if i in operators:
                operator = i
            num = ''
        else:
            num += i
    y = int(num)
    outp += ' = '
    lr = (operators.get(operator)(x, y))
    outp += str(lr)
    #outp2 = outp + ' = ' + str(lr)
    res2 = operators2.get(operator)
    return [res2, outp]
def decor(f):
    journal = open("journal.txt", "a")
    res = f(str(input()))
    operator, result = res
    journal.write("Операция: ")
    journal.write(operator)
    journal.write(", результат: ")
    journal.write(result)
    journal.write("\n")
decor(culc)


# NUMBER 2
def decor(f):
    def second(*args, **kwargs):
        journal = open("journal.txt", "a")
        operator, result = f(*args)
        journal.write("Операция: ")
        journal.write(operator)
        journal.write(", результат: ")
        journal.write(result)
        journal.write("\n")
        return f(*args, **kwargs)
    return second
def is_digit(string):
    if string.isdigit():
       return int(string)
    else:
        try:
            float(string)
            return float(string)
        except ValueError:
            return False
@decor
def culc(strForCulc):
    outp = strForCulc
    str2 = list(strForCulc)
    operators ={
        '+': (lambda x, y: x + y),
        '-': (lambda x, y: x - y),
        '*': (lambda x, y: x * y),
        '/': (lambda x, y: x / y),
        '^': (lambda x, y: x ** y)
    }
    operators2 = {
        '+': 'addition',
        '-': 'subtraction',
        '*': 'multiplication',
        '/': 'division',
        '^': 'exponentiation'
    }
    operator = ''
    num = ''
    for i in str2:
        if i in '0123456789.' and operator == '':
            num += i
        elif operator == '':
            x = int(num)
            if i in operators:
                operator = i
            num = ''
        else:
            num += i
    y = int(num)
    outp += ' = '
    lr = (operators.get(operator)(x, y))
    outp += str(lr)
    #outp2 = outp + ' = ' + str(lr)
    res2 = operators2.get(operator)
    return [res2, outp]
culc('67*8')


# NUMBER 3
import functools
def decor(f):
    @functools.wraps(f)
    def second(*args, **kwargs):
        journal = open("journal.txt", "a")
        operator, result = f(*args)
        journal.write("Операция: ")
        journal.write(operator)
        journal.write(", результат: ")
        journal.write(result)
        journal.write("\n")
        # return f(*args, **kwargs)
    return second
def is_digit(string):
    if string.isdigit():
       return int(string)
    else:
        try:
            float(string)
            return float(string)
        except ValueError:
            return False
@decor
def culc(strForCulc):
    outp = strForCulc
    str2 = list(strForCulc)
    operators ={
        '+': (lambda x, y: x + y),
        '-': (lambda x, y: x - y),
        '*': (lambda x, y: x * y),
        '/': (lambda x, y: x / y),
        '^': (lambda x, y: x ** y)
    }
    operators2 = {
        '+': 'addition',
        '-': 'subtraction',
        '*': 'multiplication',
        '/': 'division',
        '^': 'exponentiation'
    }
    operator = ''
    num = ''
    for i in str2:
        if i in '0123456789.' and operator == '':
            num += i
        elif operator == '':
            x = int(num)
            if i in operators:
                operator = i
            num = ''
        else:
            num += i
    y = int(num)
    outp += ' = '
    lr = (operators.get(operator)(x, y))
    outp += str(lr)
    #outp2 = outp + ' = ' + str(lr)
    res2 = operators2.get(operator)
    return [res2, outp]
culc('666*666')


 # VSR
import time

def time_decore(func):
    print(time.asctime(), end='')
    return func

@time_decore
def tryDecore():
    print(' - дата выполнения этой функции')

tryDecore()

