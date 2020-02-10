import sys
sys.stdin = open('Ladder2.txt','r')

dc = [-1,1]
def dir_check(r,c): #처음 0,0이 들어오면
    for i in range(2): #방향 설정은 x축으로만 이동한다.
        nc = c + dc[i]
        if nc < 0 or nc >= 100:
            continue
        if ladder[r][nc] == 1:
            return i
    return 2 #x축의 좌 우측을 보고 전체 배열을 넘어가면 건너 뛰고 좌 우측에 1이 보이면 그때의 i를 꺼냄

def go(st):
    cnt = 0
    col = st #호출된 1인 x의 인덱스가 들어온다. 처음에 0이 들어오겠지.
    for i in range(100):
        dir = dir_check(i,col) #처음에 dir_check(0,0)이 들어가면 위에 함수로 들어가
        if dir < 2: #좌우측에 1이 있을때
            while 1:
                nc = col + dc[dir] #좌 우측으로 한 번 이동
                if nc < 0 or nc >= 100 or ladder[i][nc] == 0:
                    break
                cnt +=1
                col = nc #좌 우측으로 누적 이동시키기 위해서
        cnt += 1 #dir값이 2이면 좌 우측에 아무것도 없으니 그냥 쭉 내려가며 cnt += 1
    return cnt


for t in range(10):
    tc = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]

    min_value = 987654321
    ans_idx = 987654321

    for i in range(len(ladder[0])): #x 축에서 1을 찾아낸다.
        if ladder[0][i] == 1: #만약 x축에서 1을 발견하면,
            tmp = go(i) # 값이 1인 x축의 인덱스 i를 넣는다.
            if tmp <= min_value:
                min_value = tmp
                ans_idx = i

    print('#{} {}'.format(tc,ans_idx))




