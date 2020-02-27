import sys
sys.stdin = open('maxprice.txt','r')

def gen(n):
    for i in range(n):
        yield input().strip().split()

def solve(n, count):
    number = list(map(int, n))
    # 중도에 멈춰야 하는 경우 flag를 False로 변경
    flag = True
    checkIndex = 0      # 앞부분부터 체크하고 있는 index
    targetIndex = -1    # 교환할 index
    lastIndex = len(number) - 1

    while count and flag:
        chk = number[checkIndex]
        # target이 number의 범위를 초과하는지 체크
        if checkIndex + 1 < lastIndex:
            other = max(number[checkIndex + 1:])
            otherCount = number.count(other)
            # checkIndex 값과 뒷자리의 최댓값과 값을 비교
            if chk < other:
                changeLen = 0
                # 뒤에서부터 target의 index 확인
                for i in range(lastIndex, 0, -1):
                    if number[i] == other:
                        targetIndex = i
                        break
                # targetIndex의 값이 여러개인 경우 연속되어 있는지 체크 -> ex(32)8(88) (88)8(32)
                if otherCount > 1:
                    for i in range(checkIndex, lastIndex):
                        if number[checkIndex] >= number[i]:
                            changeLen += 1
                        else:
                            break
                    # 변경할 길이는 checkIndex 부분의 감소하는 값들의 갯수, 뒷자리의 연속된 값의 갯수, 교환 가능한 count의 수 중에 최솟값
                    changeLen = min(changeLen, otherCount, count)
                    for i in range(0, changeLen):
                        if number[targetIndex] == number[targetIndex - i]:
                            break
                        else:
                            targetIndex -= 1
                    # targetIndex부터 changeLen 만큼 통째로 자리 교환
                    number = number[0:checkIndex] + number[targetIndex:targetIndex + changeLen]\
                            + number[checkIndex + changeLen:targetIndex] + number[checkIndex:checkIndex + changeLen]\
                            + number[targetIndex + changeLen:]
                    # 변경한 길이 만큼 차감
                    count -= changeLen
                else:
                    # 한 개만 바꾸면 되는 경우
                    number[checkIndex], number[targetIndex] = number[targetIndex] , number[checkIndex]
                    count -= 1  # 변경 count 차감
        checkIndex += 1
        # 마지막 index까지 갔으나 count가 남아있는 경우
        if checkIndex == lastIndex and count > 0:
            # 동일한 자리 변경이 가능하므로 변화가 없다.
            if count % 2 == 0:
                flag = False
            else:
                # 꼭 한번은 바꿔줘야 한다.
                # 동일한 숫자가 2번 이상 있는 경우 : 그 분을 교환하면 되므로 flag를 Flase로 변경
                # 동일한 숫자가 없는 경우 : 맨 마지막 두자리의 값을 변경
                for i in number:
                    if number.count(i) >= 2:
                        flag = False
                if flag:
                    number[lastIndex], number[lastIndex -1] = number[lastIndex - 1], number[lastIndex]
                    flag = False
    return ''.join(map(str, number))

num = 0
n = int(input().strip())
for n, count in gen(n):
    num += 1
    print('#{0} {1}'.format(num, solve(list(n), int(count))))
