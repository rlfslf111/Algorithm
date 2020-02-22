# import sys
# sys.stdin = open('code.txt','r')

reading = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
           '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

def Extraction(code):
    global N, M, data
    for y in range(N):
        for x in range(M-1,-1,-1):
            if code[y][x] == '1':
                data = code[y][x-55:x+1]
                return data

tc = int(input())
for t in range(tc):
    N, M = map(int,input().split())
    code = [list(input()) for _ in range(N)]
    data = ''
    Extraction(code)

    result = []
    for i in range(0,len(data),7):
        ans = ''
        for j in range(i,i+7):
            ans += data[j]
        result.append(ans)

    answer = []
    for k in range(8):
        answer.append(reading[result[k]])

    value = (answer[0]+answer[2]+answer[4]+answer[6])*3 + (answer[1]+answer[3]+answer[5]) + answer[7]

    if value % 10 == 0:
        print('#{} {}'.format(t+1,sum(answer)))
    else:
        print('#{} {}'.format(t+1,0))
