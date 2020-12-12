import time


def initial_state():
    initial_state = 'initial_state'
    return initial_state

#명령어 ' 유무 체크
def check_inputstr(input_word):
    input_word_list = list()
    for i in range(0, len(input_word)):
        if i != len(input_word)-1 and input_word[i+1] == "'":
            input_word_list.append(input_word[i] + input_word[i+1])
        elif input_word[i] != "'":
            input_word_list.append(input_word[i])
    return input_word_list



if __name__ == '__main__':
    start = time.time()
    input_count = 0
    
    #큐브 초기모습 출력자리
    print(initial_state())
    
    while True:
        input_word = str(input("CUBE > "))
        input_word_list = check_inputstr(input_word)

        if input_word == 'Q':
            elapsed_time = time.time() - start
            print("경과시간:", time.strftime("%H:%M:%S",time.gmtime(elapsed_time)))
            print("조작갯수:", input_count)
            print("이용해주셔서 감사합니다. 뚜뚜뚜.")
            break
        else:
            for action in input_word_list:
                input_count += 1
                print(action)
                #큐브 함수 만들어서 넣어줄 자리