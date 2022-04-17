def reverse_vowels(word):
    answer = ""
    reverse = []
    vowels = ["a", "e", "i", "o", "u"]
    vowels_caps = ["A", "E", "I", "O", "U"]
    for l in word:
        if l in vowels or l in vowels_caps:
            reverse.append(l)
    reverse = reverse[::-1]
    count = 0;
    x = ''
    for l in word:
        if l not in reverse:
            x += l
        if l in reverse:
            x += reverse[count]
            count += 1
    return x
    # [num[::-1] for num in ["Elie", "Tim", "Matt"]]


print(reverse_vowels("Reverse Vowels In A String"))


def running_average(number):
    running_average.accumulator = 0
    running_average.size = 0

    def inner(number):
        running_average.accumulator += number
        running_average.size += 1

        return running_average.accumulator / running_average.size

    return inner


aVrg = running_average(10)
aVrg = running_average(11)
print(aVrg)


def letter_counter(word):
    x = word.lower()
    letter_counter.accumulator = x
    print(x)

    def inner(letter):
        letter = letter.lower()
        number = 0
        for l in x:
            if l == letter:
                number += 1

        return number

    return inner


word = letter_counter("Amazing")
print(word('a'))


def once(func):
    once.accumulator = 0

    def inner(*args):
        once.accumulator += 1
        if once.accumulator == 1:
            return func(*args)
        else:
            return None

    return inner


def add(a, b):
    return a + b


oneAddition = once(add)
oneAddition(1, 2)
oneAddition(1, 2)



