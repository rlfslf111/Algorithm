import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def prize(commute, attendance, late, absent):
    # 지각이 2번 이상일 경우 수여 불가
    if 2 <= late:
        return 0

    # 결석이 3번 이상이면 수여 불가
    if 3 <= absent:
        return 0

    # 개근상 수여 조건 충족
    if attendance == commute:
        return 1

    # 출석, 지각, 결석이 다음과 같으면 개근상 수여 가능 경우의 수
    if (attendance, late, absent) in result:
        return result[(attendance, late, absent)]

    # 일정 날 되는 날, 그 이후 출석, 지각, 결석 했을 때 개근상 수여 가능 경우의 수
    result[(attendance, late, absent)] = prize(commute, attendance + 1, late, 0) + prize(commute, attendance + 1, late + 1, 0) + prize(commute, attendance + 1, late, absent + 1)
    return result[(attendance, late, absent)]

result = {}
N = int(input().strip())
print(prize(N,0,0,0)%1000000)
