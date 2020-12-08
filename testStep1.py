word, number, lr = input("Write one word, one number, L(left) or R(right):").split(' ')
number = int(number)

def push_string(word,number,lr):

# -100이상 100미만 수 걸러내기
    if -100 <= number < 100:

        #음수 체크후, 방향 설정
        if number < 0 and (lr == "L" or lr =='l'):
            number = -number
            lr = "R"
        elif number < 0 and (lr == "R" or lr == 'r'):
            number = -number
            lr = "L"

        #문자열 길이 보다 클 경우 나머지 값으로 이동시키기
        num = number % len(word)

        if lr == "L" or lr == "l":

            Lfirst = word[0: num]
            Lsecond = word[num:]

            answer = Lsecond + Lfirst

        elif lr == "R" or lr == 'r':
            Rfirst = word[0: len(word) - num]
            Rsecond = word[len(word) - num:]

            answer = Rsecond+Rfirst

    else:
        answer = "-100이상 100미만의 정수를 작성하세요."

    return answer


print(push_string(word,number,lr))











