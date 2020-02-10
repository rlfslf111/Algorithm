A = list(range(1,13))
test_case = int(input())
for t in range(test_case):
    gesu, sum_result = map(int,input().split())
    count = 0
    for i in range(1<<len(A)):
        sum = 0
        result = []
        for j in range(len(A)):
            if i & (1<<j):
                sum += A[j]
                result.append(A[j])
        if sum == sum_result:
            if len(result) == gesu:
                count+=1
    print('#{} {}'.format(t+1,count))