# This is a sample Python script.
from flask import Flask

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

app = Flask(__name__)


@app.route("/")
def index():
    def print_hi(name):
        # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # Press the green button in the gutter to run the script.
    if __name__ == '__main__':
        print_hi('Python')

    # Lambda exemple
    bing = lambda x, y: x / y
    print(bing(6, 2))

    # lambda map example
    def decrement_list(data):
        return list(map(lambda x: x - 1, data))

    print(decrement_list([33, 28, 76]))

    # filter map example
    def remove_negatives(data):
        return list(map(lambda data: data, filter(lambda u: u >= 0, data)))

    print(remove_negatives([78, 45, -66, 0, -123]))

    # Iterators

    def my_for(iterable, func):
        iterator = iter(iterable)
        while True:
            try:
                thing = next(iterator)
            except StopIteration:
                break
            else:
                func(thing)

    def square(x):
        print(x * x)

    my_for("lol", print)
    my_for([1, 2, 3, 4, 5], square)

    class Counter:
        def __init__(self, low, high):
            self.current = low
            self.high = high

        def __iter__(self):
            return self

        def __next__(self):
            if self.current < self.high:
                num = self.current
                self.current += 1
                return num
            raise StopIteration

    for x in Counter(50, 70):
        print(x)

    # Generator

    def yes_or_no():
        answer = "yes"
        while True:
            yield answer
            answer = "no" if answer == "yes" else "yes"

    def get_multiples(num=1, count=10):
        next_num = num
        while count > 0:
            yield next_num
            count -= 1
            next_num += num

    # Decorator
    def be_polite(fn):
        def wrapper():
            print("What a pleasure to meet you!")
            fn()
            print("Have a great day!")

        return wrapper

    @be_polite
    def greet():
        print("My name is Colt.")

    @be_polite
    def rage():
        print("I HATE YOU!")

    greet()
    return rage()
