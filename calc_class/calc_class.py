class Calc:
    def set_number(self, num1, num2):
        self.num1 = int(num1)
        self.num2 = int(num2)
    def plus(self):
        return self.num1 + self.num2
    def minus(self):
        return self.num1 - self.num2
    def multiple(self):
        return self.num1 * self.num2
    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError: # 0으로 나누면서 에러가 발생했을 때
            print("0으로는 나눌수 없습니다.")


num1= input("첫번째 숫자 입력: ")
num2 = input("두번째 숫자 입력: ")

try:
    int(num1)

except ValueError:  # int로 변환하는 과정에서 에러가 발생했을 떄
    print(f"{num1}은(는) 숫자만 입력 가능합니다.")

    try:
       int(num2)
       calc = Calc()
       calc.set_number(num1, num2)
    except ValueError:  # int로 변환하는 과정에서 에러가 발생했을 떄
        print(f"{num2}은(는) 숫자만 입력 가능합니다.")




print(calc.plus()) # 더한 값
print(calc.minus()) # 뺀 값
print(calc.multiple()) # 곱한 값
print(calc.divide()) # 나눈 값

