# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Myclass_1:
    #x: int
    def __init__(self,x=0):
        self.x = x

class Myclass_2:
    x: int
    def __init__(self):
        pass

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    #print('Hi,', name)  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MyObject_1 = Myclass_1()
    MyObject_1.x = 10.5
    print(MyObject_1.x)
    MyObject_2 = Myclass_2()
    MyObject_2.x = 10.5
    print (MyObject_2.x)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
