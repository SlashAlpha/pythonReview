# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
list_line = list()




for i in range(height):
    line = input()  # width characters, each either 0 or .
    list_line.append(line)

def check_node(param, x, y, width, height):
    axe = x if param else y
    length = width if param else height
    i = 1
    while (axe + i < length):
        node = list_line[y][x + i] if param else list_line[y + i][x]
        if node == "0" and param:
            return str(x + i) + " " + str(y) + " "
        elif node == "0" and not param:
            return str(x) + " " + str(y+i) + " "
        i = i + 1
    return str("-1"+" "+"-1"+" ")



for y in range(height):

    for x in range(width):
        node_formation = ""
        if list_line[y][x] == "0":
            node_formation += str(x) + " " + str(y) + " "
            node_formation += check_node(True, x, y, width, height)
            node_formation += check_node(False, x, y, width, height)
            print(node_formation)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
