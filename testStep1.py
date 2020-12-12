def push_string(word,number,lr):

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

    return answer


if __name__ == '__main__':
    while True:
        try:
            word, number, lr = input("Write one word, one number, L(left) or R(right):").split(' ')
            number = int(number)
            if -100 <= number < 100:
                print(push_string(word,number,lr))
            else:
                print("-100이상 100미만의 정수를 작성하세요.")
        except ValueError:
            print("잘못 작성하셨습니다. 다시 입력해주세요.")
            pass
