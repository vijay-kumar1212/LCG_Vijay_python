# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
fruits = list(("banana", "apple", "grapes", "jack fruit", "guava"))
print(fruits)
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1
print("#########")
[print(x) for x in fruits]
newlist = []
for x in fruits:
    if 'j' in x:
        newlist.append(x)
print(newlist)

new_list1 = [x for x in fruits if "ja" not in x]
print(new_list1)
fruits.sort()
print(fruits)
