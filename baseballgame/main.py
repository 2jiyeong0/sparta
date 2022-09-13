import random
import time
from datetime import datetime, timedelta


def main():
    # 1. 사용자의 입력을 받아 n개의 중복되지 않는 랜덤한 숫자를 생성한다.
    N = int(input("몇자리수 게임? "))
    random_list = [x for x in range(10)]    #random_numbers 변수를 list 자료형으로 선언 (0 ~ 9 범위)
    random.shuffle(random_list)
    random_numbers = random_list[:N]   # N 개만큼 랜덤변수 저장

    print(random_numbers)


    # 2. 프로그램이 시작 된 시간을 기록한다.
    start_time = time.time()

    # 3. 사용자의 입력을 받고, 입력을 받을 때마다 try count를 1씩 더해준다.
    try_count = 0

    while True:
        my_input = input("숫자 입력(exit 입력시 게임종료): ")
        if my_input == "exit":
            return

        try_count += 1
        print(f'input: {my_input} count: {try_count}')

        # 4. 사용자 입력 x와 랜덤하게 생성 된 y 두 숫자를 비교한다.
        out_count = 0
        strike_count = 0
        ball_count = 0

        #  4-a. x의 첫 번째 숫자가 y에 포함되어 있는지 확인한다.
        #   * 포함되어 있지 않다면  out count + 1 
        for i, v in enumerate(my_input):
            v = int(v)
            if v not in random_numbers:
                out_count += 1

        # #  4-b. x의 첫 번째 숫자가 y에 포함되어 있다면 x의 첫 번째 숫자와 y의 첫 번쨰 숫자가 일치하는지 확인한다.
        # #   * 일치하는 경우 strike count + 1
        # #   * 일치하지 않는 경우 ball count + 1   
            else:
                if random_numbers[i] == v:
                    strike_count += 1
                else:
                    ball_count += 1

        
            #  4-c. 4-a ~ 4-b를 x의 모든 자릿수를 돌 때까지 반복한다.
        # 5. 사용자가 exit을 입력하거나 정답을 맞출 때까지 3~4의 동작을 무한하게 반복한다.

        # 6. 사용자의 입력이 1번에서 생성한 숫자와 일치 할 경우 필요한 정보를 출력하고 프로그램을 종료한다.
        if strike_count == N:
            print("########################")
            print("정답입니다!!")
           
            #  6-a. try count를 출력한다.
            print(f"try_count :{try_count}")
            
            end_time = time.time()
            #  6-b. 프로그램이 종료 된 시간과 프로그램이 시작 된 시간의 차를 계산해 프로그램의 실행 시간을 출력한다.
            print(f"코드 실행 시간 : {end_time-start_time:.2f}")
            
            #  6-c. 게임이 종료 된 시점의 날짜와 시각을 출력한다.           
            print(f"종료시각: {datetime.now()}")
            print("########################")
            return 

        print(f"{ball_count}볼 {strike_count}스트라이크{out_count}아웃")         

main()
