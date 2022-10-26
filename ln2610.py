# 1.1
# - найти кол-во дублирующихся букв (не зависит от регистра)
import time


def find_letters(string):
    repeating_l = []
    dublicate_l = []
    count = 0

    for letter in string:
        if letter in repeating_l and letter not in dublicate_l:
            count += 1
            dublicate_l.append(letter)
        else:
            repeating_l.append(letter)

    return count


# print(find_letters('abbccc'))


# 1.2
def find_letters2(string):
    return len([ch for ch in (set(string.lower())) if string.lower().count(ch) > 1])


# print(find_letters2('abbccc'))


def worktime(f1, f2):
    def f(string):
        initial_time = time.time()
        f1(string)
        first = time.time() - initial_time
        initial_time = time.time()
        f2(string)
        second = time.time() - initial_time
        print(f1.__name__ if first < second else f2.__name__)

    return f


funcion = worktime(find_letters, find_letters2)
funcion('aaaBBnn')
