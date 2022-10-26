# 1.1
# - найти кол-во дублирующихся букв (не зависит от регистра)
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


print(find_letters('abbccc'))


# 1.2
def find_letters2(string):
    return len([ch for ch in (set(string.lower())) if string.lower().count(ch) > 1])


print(find_letters2('abbccc'))
