
from curses.ascii import isdigit


def main():

    try_count = 0

    while try_count < 5:
        my_input = input("입력(exit 입력시 프로그램 종료): ")
        if my_input == "exit":
            return
        try_count += 1
        print(type(my_input))

        if my_input.isdigit():
            print(int(my_input) * 2)

        else:
            print(f'입력한 문자는 {my_input} 입니다.')




main()