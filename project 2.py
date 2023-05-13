# a program to calculate the net income after federal tax
from gui import *

def main():
    window = Tk()
    window.title('net income calculation')
    window.geometry('300x100')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()