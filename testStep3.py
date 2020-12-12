import time


def initial_state():
    initial_state = 'initial_state'
    return initial_state



if __name__ == '__main__':
    input_count = 0
    
    #큐브 초기모습 출력자리
    print(initial_state())
    
    while True:
        start = time.time()
        input_word = str(input("CUBE > "))

        if input_word == 'Q':
            elapsed_time = time.time() - start
            print("경과시간:", time.strftime("%H:%M:%S",time.gmtime(elapsed_time)))
            print("조작갯수:", input_count)
            print("이용해주셔서 감사합니다. 뚜뚜뚜.")
            break
        else:
            for action in input_word:
                input_count += 1
                print(action)
                #큐브 함수 만들어서 넣어줄 자리
				