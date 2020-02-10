import sys
sys.stdin = open('input.txt','r')
def make_bar(start):  # 매개변수로 시작 인덱스를 입력받음
    conn = [screw[start]]  # 초기값으로 시작 나사를 넣어 놓음
    use = [0] * N  # 내가 해당 위치의 나사를 썼는지를 체크하기 위한 리스트
    use[start] = 1  # start 위치의 나사는 사용을 했기 때문에 1로 표시

    for i in range(N - 1):  # 첫번째 나사를 이미 정했기 때문에 N-1번만 돌면서 넣을 준비
        isOk = False  # 다음 나사 연결 됬는지 안됬는지 체크하기위한 변수
        # 한 사이클이 돌때매다 초기화 한다.
        for j in range(N):  # 어떤 나사가 올 수 있을지 모르니 처음부터 끝까지 반복
            # 만약 j위치의 나사를 사용하지 않았고
            # 이미연결된 conn[i]의암나사와 screw[j]의 수나사가 연결이 될 수 있다면
            if use[j] == 0 and conn[i][1] == screw[j][0]:
                # 연결을 한다.
                conn.append(screw[j])
                use[j] = 1  # j위치의 나사는 사용을 한것이므로 1로 표시
                isOk = True  # 이번 사이클에서는 연결을 한거니까 다음 반복문을 돌 준비를 한다.
                # 연결이 됬으니 반복문을 죽여버림.
                break
        # 만약 연결을 하지 못했다면 더 이상의 반복문을 도는 것은 의미가 없으니 break
        if not isOk:
            break
    # 지금까지 연결한 상태를 return 최소크기는 1이다.
    # 우리가 시작나사를 넣고 시작하니.
    return conn


T = int(input())

for tc in range(1, T + 1):
    # 나사의 갯수 N과 수나사 암나사가 적힌 입력 한줄 받기
    N = int(input())
    line = list(map(int, input().split()))

    # 입력 받은 나사의 수만큼 0으로 초기화
    screw = [0] * N
    idx = 0  # 밑에 반복이 2칸씩 뛰기 때문에 나사를 위한 인덱스
    # 사실 screw = [] 처럼 빈리스트를 선언하고 밑에서 인덱스 접근이 아니라
    # screw.append([line[i], line[i+1]을 하면 idx 변수는 필요없음.
    # 2칸씩 움직이는 반복문을 돌면서 screw 채우기
    for i in range(0, len(line), 2):
        screw[idx] = [line[i], line[i + 1]]
        idx += 1

    # 정답을 담을 공백리스트 선언
    ans = []
    # 첫번째 나사로 모든 나사를 해봐야 하기 때문에 나사 수 만큼 반복
    for i in range(N):
        # make_bar 함수를 이용해 내가 지금 만들수 있는 가장 긴 막대를 만들어
        # tmp에 임시로 저장하기
        tmp = make_bar(i)
        # tmp의 길이가 ans보다 길게 되면 더 많은 연결이 있었다는것 고로 변경
        if len(ans) < len(tmp):
            ans = tmp

    # 출력문
    print("#{}".format(tc), end=" ")
    for i in range(N):
        print("{} {}".format(ans[i][0], ans[i][1]), end=" ")
    print()




